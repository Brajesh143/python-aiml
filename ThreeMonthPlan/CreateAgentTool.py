from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain.agents import create_agent

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
)

@tool
def addition(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@tool
def multiplication(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

tools = [addition, multiplication]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful calculator assistant."
)

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Calculate 10 + 20 and explain the result."
        }
    ]
})

print(response["messages"][-1].content)