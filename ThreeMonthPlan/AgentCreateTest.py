from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain.messages import HumanMessage

llm = ChatOllama(
    model="qwen3:0.6b",
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
    tools=tools
)

response = agent.invoke({
    "messages": [
        HumanMessage(
            content="What would be the result of sum of 20 and 30 and this sum will be multiple by 2?"
        )
    ]
})
print(response["messages"][-1].content)