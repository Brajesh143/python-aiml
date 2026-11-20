from typing import TypedDict

from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langchain.agents import create_agent

# Dummy employee database
employees = {
    101: {
        "name": "Rahul",
        "leave_balance": 10
    }
}

@tool
def get_leave_balance(employee_id: int) -> str:
    """Get the available leave balance of an employee."""

    employee = employees.get(employee_id)

    if not employee:
        return "Employee not found."

    return f"{employee['leave_balance']} leave days available."


@tool
def apply_for_leave(employee_id: int, days: int) -> str:
    """Submit a leave request for an employee."""

    employee = employees.get(employee_id)

    if not employee:
        return "Employee not found."

    if days <= 0:
        return "Invalid leave duration."

    if days > employee["leave_balance"]:
        return "Insufficient leave balance."

    return f"Leave request for {days} days submitted successfully."

llm = ChatOllama(
    model="qwen3:0.6b",
    temperature=0
)

tools = [
    get_leave_balance,
    apply_for_leave
]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
    You are an HR Assistant.

    The employee ID is 101.

    Help employees with leave-related queries.

    Use tools to check leave balance
    and submit leave requests.

    Never invent employee information.
    """
)

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "What is my leave balance?"
        }
    ]
})

print(response["messages"][-1].content)