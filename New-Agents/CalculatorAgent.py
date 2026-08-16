from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.agents import create_agent
from langchain_core.tools import tool

model = ChatOllama(model="qwen3:8b")

@tool
def calculate(operation: str, a: float, b: float) -> float:
    """Perform a mathematical operation on two numbers."""

    if operation == 'add':
        return a + b

    elif operation == 'subtract':
        return a -b

    elif operation == 'multiply':
        return a * b

    elif operation == 'divide':
        if b == 0:
            raise ValueError("Can not divided by zero")
        return a / b

    else:
        raise ValueError("Unsupported operation, We are supporting only add, subtract, multiply and divide")

tools = [calculate]

agent = create_agent(
    model=model,
    tools=tools,
    # This is optional parameter
    system_prompt=(
        "You are a helpful assistant. "
        "Use the calculate tool to do the calculations"
    )
)

# print(agent)


result = agent.invoke({
    "messages": [
            {
                "role": "user",
                "content": "What is 125 multiplied by 24?"
            }
        ]
})

# print("----------- \n")
# print(result)
print(result["messages"][-1].content)