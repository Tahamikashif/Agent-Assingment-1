from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set
from dotenv import load_dotenv
import asyncio
import os


load_dotenv(override=True)
gemini_api = os.getenv("GEMINI_API_KEY")
if not gemini_api:
    raise ValueError("Gemini api is not found")

client = AsyncOpenAI(api_key=gemini_api,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

Model = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=client)

agent = Agent(name="Ratan lal",instructions="You are my helpful assistant",model=Model)

async def main():
    result = await Runner.run(starting_agent=agent,input=input("Enter your Sentences::"))
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())