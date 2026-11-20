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

@tool
def substract(a: int, b: int) -> int:
    """The substtract tool will take two arguments and retur the substract result"""

    return a - b

@tool
def division(a: int, b: int) ->  float:
    """The division tool will take two arguments and return the divided answer """

    return a / b

tools = [multiply, addition, substract, division]

tool_with_name = {
    tool.name: tool for tool in tools
}

tool_with_llm = llm.bind_tools(tools)

prompt = input("Enter your question \n")

tool_call_data = tool_with_llm.invoke(prompt)

if tool_call_data.tool_calls:
    # params = tool_call_data.tool_calls[0]

    # selected_tool = tool_with_name[params["name"]]

    # result = selected_tool.invoke(params)

    # print(result.content)

    print(tool_call_data.tool_calls)

    for tool_call in tool_call_data.tool_calls:

        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        selected_tool = tool_with_name.get(tool_name)

        if selected_tool:
            result = selected_tool.invoke(tool_args)

            print(f"Tool: {tool_name}")
            print(f"Result: {result}")

else:
    print(tool_call_data.content)