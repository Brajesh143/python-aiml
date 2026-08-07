import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Statement to fact-check
statement = "The Great Wall of China is visible from the Moon."

# Prompt for the agent
prompt = f"""
You are a fact-checking AI agent.

Steps:
1. Decide if the statement is TRUE, FALSE, or UNCERTAIN.
2. Give a short explanation (2–3 lines).
3. Mention well-known sources if applicable.

Statement:
"{statement}"
"""

# Call Gemini model
response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents=prompt
)

# Output result
print("\nFACT CHECK RESULT:\n")
print(response.text)
