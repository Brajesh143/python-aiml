from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool

model = ChatOllama(model="qwen3:8b")

@tool
def calculate(operation: str, a: float, b: float) -> float:
    """Perform a mathematical operation on two numbers"""

    operation = operation.lower().strip()

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            raise ValueError("Can not divide by 0.")
        return a / b

    else:
        raise ValueError("We are supporting only add, subtract, multiply and divide operations!")

tools = [calculate]

model_with_tool = model.bind_tools(tools)

query = HumanMessage("What is 125 multiplied by 24?")

messages = [query]

model_result = model_with_tool.invoke(messages)

print(model_result.tool_calls[0])

args =model_result.tool_calls[0]["args"]

final_result = calculate.invoke(args)

print(final_result)