import chainlit as cl
from main import agent
from agents import Runner


@cl.on_chat_start
async def on_chat_start():

    await cl.Message(content=f"This agent created by **Tahami Software Engineer**").send()

@cl.on_message
async def on_message(message:cl.Message):
    prompt = message.content
    result = await Runner.run(agent,prompt)

    await cl.Message()
