import os
from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel , AsyncOpenAI , RunConfig

# -------------------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# -------------------

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# -------------------


client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

config = RunConfig(
     model = OpenAIChatCompletionsModel(
         model="gemini-2.0-flash",
         openai_client= client
    ),
    model_provider=client,
    tracing_disabled=True
)