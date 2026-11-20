from langchain_ollama import ChatOllama
from langchain.tools import tool

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

tools = [multiply, addition]

tool_with_llm = llm.bind_tools(tools)

prompt = "What would be the addition of 10 and 20?"

tool_call = tool_with_llm.invoke(prompt)

if tool_call.tool_calls:

    params = tool_call.tool_calls[0]

    tools_by_name = {
        tool.name: tool for tool in tools
    }

    selected_tool = tools_by_name[params["name"]]

    result = selected_tool.invoke(params)

    print(result.content)

else:
    print(tool_call.content)