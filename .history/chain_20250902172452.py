# import chainlit as cl
# from main import agent
# from agents import Runner


# @cl.on_chat_start
# async def on_chat_start():

#     await cl.Message(content=f"This agent created by **Tahami Software Engineer**").send()

# @cl.on_message
# async def on_message(message:cl.Message):
#     prompt = message.content
#     result = await Runner.run(agent,prompt)

#     await cl.Message(content="Translating...").send()

#     await cl.Message(content=f"Received:{result.final_output}").send()
import chainlit as cl
from main import agent
from agents import Runner


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content=f"This agent created by **Tahami Software Engineer**").send()


# @cl.on_message
# async def on_message(message: cl.Message):
#     prompt = message.content.strip()

#     # Agar user "test" bhejta hai, to 5 sawalat run karenge
#     if prompt.lower() == "test":
#         questions = [
            # "What is GitHub?",
            # "Who created Python?",
            # "What is the capital of Japan?",
            # "Explain what an API is in simple terms.",
            # "What is the difference between AI and Machine Learning?"
#         ]

        # await cl.Message(content="🧪 Running 5 test questions...").send()

#         for q in questions:
#             # Sawal send karo
#             await cl.Message(content=f"❓ {q}").send()

#             # Agent run karo
#             result = await Runner.run(agent, q)

#             # Answer show karo
#             await cl.Message(content=f"💡 {result.final_output}").send()

#     else:
#         # Normal chat flow
#         result = await Runner.run(agent, prompt)

#         await cl.Message(content="Translating...").send()
#         await cl.Message(content=f"Received: {result.final_output}").send()

@cl.on_message
async def on_message(message:cl.Message):
    prompt = message.content.strip()

    if prompt.lower == "test":
     questions = [
        "What is GitHub?",
            "Who created Python?",
            "What is the capital of Pakistan?",
            "Explain what an API is in simple terms.",
            "What is the difference between AI and Machine Learning?"
    ]

    await cl.Message(content="🧪 Running 5 test questions...").send()

    for q in questions:
       await cl.Message(content=f"❓ {q}").send()



    result = await Runner.run(agent,prompt)

    await cl.Message(content=f"Received:{result.final_output}").send()


   else:

   
      
