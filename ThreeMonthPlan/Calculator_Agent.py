from langchain_ollama import ChatOllama
from langchain.tools import tool
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph import START, END, MessagesState, StateGraph

llm = ChatOllama(
    model="qwen3:0.6b",
    temperature=0
)

@tool
def multiply(a: int, b: int) -> int:
    """This tool will take two parameters a and b, return the multiplication of those two parameters"""
    return a * b

@tool
def addition(a: int, b: int) -> int:
    """The additional_tool will use to take two integer parameters and return their sum"""

    return a + b

@tool
def substract(a: int, b: int) -> int:
    """The substtract tool will take two arguments and retur the substract result"""

    return a - b

@tool
def division(a: int, b: int) ->  float:
    """The division tool will take two arguments and return the divided answer """

    if b == 0:
        return "We can't didvide by zero"
    
    return a / b

tools = [multiply, addition, substract, division]

tool_with_llm = llm.bind_tools(tools)

tool_node = ToolNode(tools)

def chatbot(state: MessagesState):
    response = tool_with_llm.invoke(
        state["messages"]
    )
    return {"messages": [response]}

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
            "content": "Calculate 100 - 45"
        }
    ]
})

print(response["messages"][-1].content)