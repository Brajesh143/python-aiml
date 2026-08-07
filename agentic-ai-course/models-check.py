import os
from dotenv import load_dotenv
from google.genai import Client

load_dotenv()

client = Client(api_key=os.getenv("GEMINI_API_KEY"))

for m in client.models.list():
    print(m.name)
