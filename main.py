
import openai
import chainlit as cl

openai.api_key = "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"

model_name = "text-davinci-003"

settings = {
    "temperature": 0.7,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stop": ["```"],
}

prompt = """

Act like chatbot

1.you are vehical insurance Asistant discount  you give discount to user on the basis of there certfication score.



2.certification score and there discount range.

     2.1 if user get score between ( 80 to 100 ) percent prvoide them 15 % discount.
     2.2 if user get certification score between ( 60 to 80 ) percent provide them 10 % discount
     2.3 if user get certification score below 60 % dont give an discount.

3.some improtnant point ask to user one by one like chatbot before providing discount and then calculate discount and provide to user.
    3.1 Ask user to there name 
    3.2 last four digit of policy number
    3.3 certfication score
    3.4vcalculate discount to user's policy and inform them of the new premium cost.

{question}
"""


@cl.on_message
async def main(message: str):
    fromatted_prompt = prompt.format(question=message)
    msg = cl.Message(
        content="",
    )

    async for stream_resp in await openai.Completion.acreate(
        model=model_name, prompt=fromatted_prompt, stream=True, **settings
    ):
        token = stream_resp.get("choices")[0].get("text")
        await msg.stream_token(token)

    await msg.send()
