from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
from langchain.tools import tool
from langchain_ollama import ChatOllama

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

# LLM node
def chatbot(state: MessagesState):
    response = llm.bind_tools(tools).invoke(
        state["messages"]
    )
    return {"messages": [response]}

# Tool execution node
tool_node = ToolNode(tools)

# Build graph
builder = StateGraph(MessagesState)

builder.add_node("chatbot", chatbot)
builder.add_node("tools", tool_node)

builder.add_edge(START, "chatbot")

builder.add_conditional_edges(
    "chatbot",
    tools_condition
)

builder.add_edge("tools", "chatbot")

graph = builder.compile()

response = graph.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Calculate 10 + 20 and explain the result."
        }
    ]
})

print(response["messages"][-1].content)