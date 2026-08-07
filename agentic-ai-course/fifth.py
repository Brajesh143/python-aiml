import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

fact_checker_instructions = """
Context:
You are a fact-checker who verifies the accuracy of statements.
Instructions:
When given statements, carefully analyze their factual accuracy using your knowledge.
Input:
You will receive statements that require fact-checking.
Output:
Respond with for each statement:
1. A verdict prefix: either "✅ TRUE:" or "❌ FALSE:"
2. A brief, one-sentence explanation justifying your conclusion
"""

statement = input("Enter statements to fact-check (separate multiple statements with semicolons): ")

prompt = f"""
{fact_checker_instructions}
statements:
"{statement}"
"""

response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents=prompt
)

print("\n🤖 Agent's Response:\n")
print(response.text)