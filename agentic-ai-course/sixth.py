import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=gemini_api_key)

calculator_instructions = """
Context:
You have to act as a calculator that will perform some artithmatic calculations.

Instructions:
When given a mathematical expression, carefully compute the result.

Input:
You will receive a mathematical expression that requires calculation.

Output:
Respond with:
1. The result of the calculation
2. A brief, one-sentence explanation of how you arrived at the result
"""

statement = input("Enter mathematical expressions to calculate (separate multiple expressions with semicolons): ")

prompt = f"""
{calculator_instructions}
statements:
"{statement}"
"""

response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents=prompt
)

print("\n🤖 Agent's Response:\n")
print(response.text)