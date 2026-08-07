import os
from dotenv import load_dotenv
from google.genai import Client

# Load environment variables
load_dotenv()

# Create Gemini client
client = Client(api_key=os.getenv("GEMINI_API_KEY"))

print("🤖 Gemini Agent started (type 'exit' to stop)\n")

AGENT_ROLE = "You are a helpful AI agent. Answer clearly and concisely."

while True:
    user_input = input("User: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Agent: Goodbye 👋")
        break

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=f"""
        {AGENT_ROLE}

        User Question:
        {user_input}

        Agent Response:
        """
    )

    print("\nAgent:", response.text, "\n")
