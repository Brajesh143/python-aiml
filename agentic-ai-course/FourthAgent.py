import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)
print("Gemini client successfully configured.")

fact_checker_instructions = """
Context:
You are a fact-checker who verifies the accuracy of statements.

Instructions:
When given a statement, carefully analyze its factual accuracy using your knowledge.

Input:
You will receive a statement that requires fact-checking.

Output:
Respond with:
1. A verdict prefix: either "✅ TRUE:" or "❌ FALSE:"
2. A brief, one-sentence explanation justifying your conclusion
"""

# A statement we want the Fact Checker agent to verify
statement = "The Great Wall of China is visible from space with the naked eye."

# Prompt for the agent
prompt = f"""
{fact_checker_instructions}
Statement:
"{statement}"
"""

# Call Gemini model
response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents=prompt
)

# Output result
print("\n🤖 Agent's Response:\n")
print(response.text)