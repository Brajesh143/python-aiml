from langgraph.graph import (
    StateGraph,
    START,
    END,
    MessagesState
)

from langgraph.prebuilt import (
    ToolNode,
    tools_condition
)
from langchain_ollama import ChatOllama

from langchain_core.messages import HumanMessage
from langchain.tools import tool

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

# LLM with tools
llm_with_tools = llm.bind_tools(tools)

# Agent node
def agent_node(state: MessagesState):
    response = llm_with_tools.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }

# Create graph
builder = StateGraph(MessagesState)

builder.add_node("agent", agent_node)

builder.add_node(
    "tools",
    ToolNode(tools)
)

builder.add_edge(START, "agent")

builder.add_conditional_edges(
    "agent",
    tools_condition
)

builder.add_edge("tools", "agent")

graph = builder.compile()

response = graph.invoke({
    "messages": [
        HumanMessage(
            content="What would be the result of sum of 20 and 30 and this sum will be multiple by 2?"
        )
    ]
})
print(response["messages"][-1].content)