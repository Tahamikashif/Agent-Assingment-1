from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI
from dotenv import load_dotenv
import os


load_dotenv(override=True)
gemini_api = os.getenv("GEMINI_API_KEY")
if not gemini_api:
    raise V