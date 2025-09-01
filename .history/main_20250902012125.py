from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI
from dotenv import load_dotenv
import os


load_dotenv(override=True)
gemini_api = os.getenv("GEMINI_API_KEY")
if not gemini_api:
    raise ValueError("Gemini api is not found")

client = AsyncOpenAI(api_key=gemini_api,base_url="https://generativelanguage.googleapis.com/v1beta")