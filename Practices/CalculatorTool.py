from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

@tool
def calculator(operation: str, num1: float, num2: float) -> float:
    """A simple calculator that adds, subtracts, multiplies, and divides two numbers."""

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2

    else:
        return "Invalid operation. Please choose from add, subtract, multiply, or divide."


model = ChatOllama(
    model="qwen3:8b",
    temperature=0
)

tools = [calculator]

question = "What is the result of adding 5 and 3?"

message = HumanMessage(content=question)

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=(
        "You are a helpful assistant. "
        "Use the calculator tool when the user asks for calculations."
    )
)

print(agent)

result = agent.invoke({
    "messages": [message]
})

print(result["messages"][-1].content)
