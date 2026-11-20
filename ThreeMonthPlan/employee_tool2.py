from langgraph.prebuilt import ToolNode
from langchain.tools import tool
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:0.6b",
    temperature=0
)


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

tool_node = ToolNode(tools)

print(tool_node)

# result = tool_node.invoke({
#     "messages": [response]
# })

# print(result)
