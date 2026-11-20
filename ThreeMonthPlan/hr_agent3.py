
from typing import TypedDict, Annotated

from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

from langchain.agents import create_agent

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


# --------------------------------
# 1. Dummy Employee Database
# --------------------------------

employees = {
    101: {
        "name": "Rahul",
        "leave_balance": 10
    }
}


# --------------------------------
# 2. Define Tools
# --------------------------------

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

    employee["leave_balance"] -= days

    return (
        f"Leave request for {days} days submitted successfully. "
        f"Remaining balance: {employee['leave_balance']} days."
    )


@tool
def get_employee_details(employee_id: int) -> str:
    """Get employee name, ID and leave balance."""

    employee = employees.get(employee_id)

    if not employee:
        return "Employee not found."

    return (
        f"Employee ID: {employee_id}\n"
        f"Name: {employee['name']}\n"
        f"Leave Balance: {employee['leave_balance']} days"
    )


# --------------------------------
# 3. Initialize LLM
# --------------------------------

llm = ChatOllama(
    model="qwen3:0.6b",
    temperature=0
)


tools = [
    get_leave_balance,
    apply_for_leave,
    get_employee_details
]


# --------------------------------
# 4. Create Agent
# --------------------------------

hr_agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
    You are an HR Assistant.

    The employee ID is 101.

    Help employees with leave-related queries.

    Available operations:
    1. Check leave balance.
    2. Apply for leave.
    3. Get employee details.

    Use tools to perform these operations.

    Never invent employee information.

    Only report successful leave applications
    when the tool confirms success.
    """
)


# --------------------------------
# 5. Define Parent Graph State
# --------------------------------

class HRState(TypedDict):
    messages: Annotated[list, add_messages]


# --------------------------------
# 6. Define Agent Node
# --------------------------------

def hr_agent_node(state: HRState):

    # Invoke the existing create_agent agent
    result = hr_agent.invoke({
        "messages": state["messages"]
    })

    # Return only the final response
    return {
        "messages": [
            result["messages"][-1]
        ]
    }


# --------------------------------
# 7. Build Parent LangGraph
# --------------------------------

builder = StateGraph(HRState)

# Register agent as a node
builder.add_node("hr_agent", hr_agent_node)

# Define workflow
builder.add_edge(START, "hr_agent")

builder.add_edge("hr_agent", END)

# Compile
hr_graph = builder.compile()


# --------------------------------
# 8. Invoke Parent Graph
# --------------------------------

def run_agent(query: str):

    response = hr_graph.invoke({
        "messages": [
            HumanMessage(content=query)
        ]
    })

    print("\nHR Assistant:")
    print(response["messages"][-1].content)


# --------------------------------
# 9. Test Queries
# --------------------------------

if __name__ == "__main__":

    run_agent("What is my leave balance?")

    run_agent("Show my employee details.")

    run_agent("Apply for 3 days of leave.")
