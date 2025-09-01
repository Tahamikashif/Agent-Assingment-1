from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI
from dotenv import load_dotenv
import os


load_dotenv(override=True)
gemini_api = os.getenv("GEMINI_API_KEY")
if not gemini_api:
    raise ValueError("Gemini api is not found")

client = AsyncOpenAI(api_key=gemini_api,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

Model = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=client)

agent = Agent(instructions="You are my helpful assistant")

async def main():
    result = await Runner.run(starting_agent=agent,input=input("Enter your Sentences"))