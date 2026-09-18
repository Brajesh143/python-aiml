from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from langchain_ollama import ChatOllama
from langchain_core.tools import tool

LLM_MODEL = "qwen3:0.6b"

llm = ChatOllama(model=LLM_MODEL)

employees = {
    "rahul": {
        "name": "Rahul",
        "role": "Backend Developer",
        "salary": 80000,
        "department": "Engineering"
    },
    "priya": {
        "name": "Priya",
        "role": "Frontend Developer",
        "salary": 75000,
        "department": "Engineering"
    },
    "amit": {
        "name": "Amit",
        "role": "DevOps Engineer",
        "salary": 90000,
        "department": "Infrastructure"
    }
}

@tool
def get_employee(employee_name: str) -> str:
    """Get general information about an employee."""

    employee = employees.get(
        employee_name.lower().strip()
    )

    if not employee:
        return f"Employee {employee_name} not found."

    return (
        f"Name: {employee['name']}\n"
        f"Role: {employee['role']}\n"
        f"Department: {employee['department']}"
    )


@tool
def get_salary(employee_name: str) -> str:
    """Get the salary of an employee."""

    employee = employees.get(
        employee_name.lower().strip()
    )

    if not employee:
        return f"Employee {employee_name} not found."

    return f"{employee['name']}'s salary is ₹{employee['salary']}"


@tool
def get_department(employee_name: str) -> str:
    """Get the department of an employee."""

    employee = employees.get(
        employee_name.lower().strip()
    )

    if not employee:
        return f"Employee {employee_name} not found."

    return f"{employee['name']} works in {employee['department']} department."

class AgentState(TypedDict):
    question: str
    employee_name: str
    result: str


def router(state: AgentState):

    question = state["question"].lower()

    if "salary" in question or "pay" in question:
        return "salary"

    elif "department" in question:
        return "department"

    else:
        return "employee"

def employee_node(state: AgentState):

    result = get_employee.invoke({
        "employee_name": state["employee_name"]
    })

    return {
        "result": result
    }

def salary_node(state: AgentState):

    result = get_salary.invoke({
        "employee_name": state["employee_name"]
    })

    return {
        "result": result
    }

def department_node(state: AgentState):

    result = get_department.invoke({
        "employee_name": state["employee_name"]
    })

    return {
        "result": result
    }

graph = StateGraph(AgentState)

graph.add_node("employee", employee_node)
graph.add_node("salary", salary_node)
graph.add_node("department", department_node)

graph.add_conditional_edges(
    START,
    router,
    {
        "employee": "employee",
        "salary": "salary",
        "department": "department"
    }
)


graph.add_edge("employee", END)
graph.add_edge("salary", END)
graph.add_edge("department", END)

app = graph.compile()

result = app.invoke({
    "question": "Which department does Priya work in?",
    "employee_name": "Priya"
})

print(result["result"])