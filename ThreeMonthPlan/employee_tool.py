from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain.tools import tool
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:0.6b",
    temperature=0
)

# class EmployeeState(TypedDict):
#     employee_id: int
#     result: str

employees = {
    101: {
        "name": "Rahul",
        "department": "Engineering",
        "salary": 80000
    },
    102: {
        "name": "Priya",
        "department": "HR",
        "salary": 65000
    },
    103: {
        "name": "Amit",
        "department": "Finance",
        "salary": 70000
    }
}

@tool
def get_employee_details(employee_id: int) -> str:
    """Get employee name, department and salary."""

    employee = employees.get(employee_id)

    if not employee:
        return "Employee not found."

    return (
        f"Employee ID: {employee_id}\n"
        f"Name: {employee['name']}\n"
        f"Department: {employee['department']}\n"
        f"Salary: ${employee['salary']}"
    )

@tool
def get_employee_department(employee_id: int) -> str:
    """Get employee department."""

    employee = employees.get(employee_id)

    if not employee:
        return "Employee not found."

    return f"{employee['name']} works in the {employee['department']} department."

@tool
def get_employee_salary(employee_id: int) -> str:
    """Get employee salary."""

    employee = employees.get(employee_id)

    if not employee:
        return "Employee not found."

    return f"{employee['name']}'s salary is ${employee['salary']}."


tools = [
    get_employee_details,
    get_employee_department,
    get_employee_salary
]

llm_with_tools = llm.bind_tools(tools)

response = llm_with_tools.invoke(
    "What department does employee 101 work in?"
)

# print(response)

tool_call = response.tool_calls[0]

print(tool_call)

result = get_employee_department.invoke(
    tool_call["args"]
)

print(result)

# tool_node = ToolNode(tools)


# def select_tool(state: EmployeeState):

#     employee_id = state["employee_id"]

#     return {
#         "employee_id": employee_id
#     }


# graph = StateGraph(EmployeeState)

# graph.add_node("select_tool", select_tool)

# graph.add_edge(START, "select_tool")

# This example only illustrates the ToolNode.
# ToolNode expects AIMessage tool_calls, so the selection
# node must produce an AIMessage containing a tool call
# before routing to ToolNode.