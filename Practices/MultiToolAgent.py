from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

model = ChatOllama(
    model="qwen3:8b",
    temperature=0.3
)

users = {
    1: {"name": "John", "role": "admin"},
    2: {"name": "Mike", "role": "user"}
}

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
    
@tool
def get_user_by_id(user_id: int):
    """
    Get user information by user ID.
    """
    return users.get(user_id, "User not found.")

tools = [calculator, get_user_by_id]

message = input("Enter your question: \n")

messages = [HumanMessage(content=message)]

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=(
        "You are a helpful assistant. "
        "Use the get_user_by_id tool when the user asks for user information."
        "use the calculator tool when the user asks for calculations."
    )
)

result = agent.invoke({
    "messages": messages
})

print(result["messages"][-1].content)