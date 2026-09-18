from langchain_core.tools import tool
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


employees = {
    "101": {
        "name": "Rahul",
        "department": "Engineering",
        "manager": "Amit"
    },
    "102": {
        "name": "Priya",
        "department": "HR",
        "manager": "Neha"
    }
}


@tool
def get_employee(employee_id: str) -> str:
    """Get employee information."""

    employee = employees.get(employee_id)

    if not employee:
        return f"Employee {employee_id} not found."

    return (
        f"Name: {employee['name']}, "
        f"Department: {employee['department']}, "
        f"Manager: {employee['manager']}"
    )


@tool
def get_department(employee_id: str) -> str:
    """Get employee department."""

    employee = employees.get(employee_id)

    if not employee:
        return f"Employee {employee_id} not found."

    return employee["department"]


@tool
def get_manager(employee_id: str) -> str:
    """Get employee manager."""

    employee = employees.get(employee_id)

    if not employee:
        return f"Employee {employee_id} not found."

    return employee["manager"]

leave_balances = {
    "101": 12,
    "102": 8
}

attendance = {
    "101": "Present",
    "102": "Present"
}


@tool
def get_leave_balance(employee_id: str) -> str:
    """Get employee leave balance."""

    balance = leave_balances.get(employee_id)

    if balance is None:
        return f"Employee {employee_id} not found."

    return f"Employee {employee_id} has {balance} leave days remaining."


@tool
def get_attendance(employee_id: str) -> str:
    """Get employee attendance status."""

    status = attendance.get(employee_id)

    if status is None:
        return f"Employee {employee_id} not found."

    return f"Employee {employee_id} is currently {status}."

@tool
def apply_leave(employee_id: str, days: int) -> str:
    """Apply leave for an employee."""

    balance = leave_balances.get(employee_id)

    if balance is None:
        return f"Employee {employee_id} not found."

    if days > balance:
        return "Insufficient leave balance."

    leave_balances[employee_id] -= days

    return (
        f"Leave applied successfully for employee {employee_id}. "
        f"Remaining balance: {leave_balances[employee_id]}"
    )

class AgentState(TypedDict):
    question: str
    employee_id: str
    agent_type: str
    result: str


def supervisor(state: AgentState):

    question = state["question"].lower()

    if "leave" in question or "attendance" in question:
        return {
            "agent_type": "hr"
        }

    if "department" in question or "manager" in question:
        return {
            "agent_type": "employee"
        }

    if "apply" in question:
        return {
            "agent_type": "action"
        }

    return {
        "agent_type": "unknown"
    }

def employee_agent(state: AgentState):

    question = state["question"].lower()
    employee_id = state["employee_id"]

    if "department" in question:

        result = get_department.invoke({
            "employee_id": employee_id
        })

    elif "manager" in question:

        result = get_manager.invoke({
            "employee_id": employee_id
        })

    else:

        result = get_employee.invoke({
            "employee_id": employee_id
        })

    return {
        "result": result
    }


def hr_agent(state: AgentState):

    question = state["question"].lower()
    employee_id = state["employee_id"]

    if "leave" in question:

        result = get_leave_balance.invoke({
            "employee_id": employee_id
        })

    elif "attendance" in question:

        result = get_attendance.invoke({
            "employee_id": employee_id
        })

    else:

        result = "HR request not understood."

    return {
        "result": result
    }


def action_agent(state: AgentState):

    question = state["question"].lower()
    employee_id = state["employee_id"]

    if "apply leave" in question:

        result = apply_leave.invoke({
            "employee_id": employee_id,
            "days": 2
        })

        return {
            "result": result
        }

    return {
        "result": "Action not understood."
    }


graph = StateGraph(AgentState)


graph.add_node("supervisor", supervisor)
graph.add_node("employee_agent", employee_agent)
graph.add_node("hr_agent", hr_agent)
graph.add_node("action_agent", action_agent)


graph.add_edge(START, "supervisor")


graph.add_conditional_edges(
    "supervisor",
    lambda state: state["agent_type"],
    {
        "employee": "employee_agent",
        "hr": "hr_agent",
        "action": "action_agent"
    }
)

workflow = graph.compile()

result = workflow.invoke({
    "question": "What is Rahul's leave balance?",
    "employee_id": "101",
    "agent_type": "",
    "result": ""
})

print(result["result"])