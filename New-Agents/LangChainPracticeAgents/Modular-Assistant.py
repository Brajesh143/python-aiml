# Agent 2: Modular Assistant
# Build:
# Prompt → Model → Tool → Parser
# Example:
# Give me an explanation and calculate a related value.
# Focus: Understanding how LangChain components fit together.


from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.tools import tool
from langchain_core.runnables import RunnableLambda

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

model_with_tool = model.bind_tools([calculate])

template = PromptTemplate(
    template="Do the calculation by using the calculate tool and explain the {topic}",
    input_variables=["topic"]
)

def execute_calculation(message):
    tool_call = message.tool_calls[0]

    result = calculate.invoke(
        tool_call["args"]
    )

    return result


tool_executor = RunnableLambda(execute_calculation)

parser = StrOutputParser()

chain = template | model_with_tool | tool_executor

result = chain.invoke({"topic": "What is multiplication? Calculate 10 multiplied by 20."})

print(result)

