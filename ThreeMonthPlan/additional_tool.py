from langchain.tools import tool

@tool
def additional_tool(a: int, b: int) -> int:
    """The additional_tool will use to take two integer parameters and return their sum"""

    return a + b

result =  additional_tool.invoke({
    "a": 10,
    "b": 30
})

print(result)