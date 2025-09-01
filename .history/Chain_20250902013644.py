import chainlit as cl
from main import agent


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content=f"This agent created by **Tahami Software Engineer**").s