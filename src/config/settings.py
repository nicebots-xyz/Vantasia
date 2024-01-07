import os
import logging
import openai

from sqlalchemy.engine import URL
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

DATABASE_URL = URL(
    "cockroachdb+asyncpg",
    username=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_HOST"),
    port=os.getenv("DATABASE_PORT"),
    database=os.getenv("DATABASE_NAME"),
    query={"ssl": "verify-full"},
)
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DOWNLOAD_PATH = os.path.abspath("./data/downloads")
OPENAI_KEY = os.getenv("OPENAI_KEY")
openaiClient = openai.AsyncOpenAI(api_key=OPENAI_KEY, max_retries=5)

with open(os.path.join(os.path.dirname(__file__), "anthropic_prompt.txt")) as f:
    ANTHROPIC_PROMPT = f.read()

with open(os.path.join(os.path.dirname(__file__), "openai_prompt.txt")) as f:
    OPENAI_PROMPT = f.read()
ANTHROPIC_KEY = os.getenv("ANTHROPIC_KEY")
TOS_HASH = os.getenv("TOS_HASH")
TOS_URL = "https://nicebots.xyz/featured-bots/Vantasia/tos.html"
