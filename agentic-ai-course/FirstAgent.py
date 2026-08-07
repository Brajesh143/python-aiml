import asyncio
import os
from openai import OpenAI
from agents import Agent
from agents import Runner
from IPython.display import display, Markdown

from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# Let's configure the OpenAI Client using our key
openai_client = OpenAI(api_key = openai_api_key)
print("OpenAI client successfully configured.")

# A Function used to Show the given text using Markdown formatting in a Jupyter notebook
def print_markdown(text):
    """Displays text as Markdown in Jupyter."""
    display(Markdown(text))

async def main():
    print_markdown("## OpenAI Client Configured Successfully! 🎉")

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

    fact_checker_agent = Agent(
        name="FactChecker",
        instructions=fact_checker_instructions,
        model = "gpt-4.1-mini"
    )

    print(f"Agent '{fact_checker_agent.name}' created successfully!")

    # A statement we want the Fact Checker agent to verify
    statement = "The Great Wall of China is visible from space with the naked eye."

    print_markdown(f"Asking the Fact Checker to verify: '{statement}'")

    response = await Runner.run(
        starting_agent = fact_checker_agent,  # The agent we created earlier
        input = statement                 # The statement we want it to fact-check
    )

    # Display the agent's response
    print_markdown("\n🤖 Agent's Response:\n")
    print_markdown(response.final_output)

# Run the async main function
asyncio.run(main())  