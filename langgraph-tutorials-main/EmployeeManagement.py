
from typing import TypedDict, Optional, Literal

from langgraph.graph import StateGraph, START, END


# -----------------------------------
# 1. Define shared state
# -----------------------------------

class LeaveState(TypedDict, total=False):
    emp_id: str
    query: str
    requested_days: int

    leave_balance: int
    leave_type: str

    eligibility: str
    approval_status: str

    response: str


# -----------------------------------
# 2. Parallel nodes
# -----------------------------------

def get_leave_balance(state: LeaveState):
    print("Fetching leave balance...")

    # Simulate Leave Balance API
    return {
        "leave_balance": 10
    }


def get_leave_type(state: LeaveState):
    print("Identifying leave type...")

    # Simulate leave type extraction
    return {
        "leave_type": "annual"
    }


# -----------------------------------
# 3. Eligibility validation
# -----------------------------------

def check_leave_eligibility(state: LeaveState):

    balance = state["leave_balance"]
    requested_days = state["requested_days"]

    if balance >= requested_days:
        return {
            "eligibility": "eligible"
        }

    return {
        "eligibility": "insufficient"
    }


# -----------------------------------
# 4. Conditional routing
# -----------------------------------

def route_eligibility(
    state: LeaveState
) -> Literal["eligible", "insufficient"]:

    if state["eligibility"] == "eligible":
        return "eligible"

    return "insufficient"


# -----------------------------------
# 5. Manager approval
# -----------------------------------

def get_manager_approval(state: LeaveState):

    print("Requesting manager approval...")

    # Simulate Manager API
    return {
        "approval_status": "approved"
    }


# -----------------------------------
# 6. Approval routing
# -----------------------------------

def route_approval(
    state: LeaveState
) -> Literal["approved", "rejected"]:

    if state["approval_status"] == "approved":
        return "approved"

    return "rejected"


# -----------------------------------
# 7. Final action nodes
# -----------------------------------

def create_leave_request(state: LeaveState):

    print("Creating leave request...")

    # Simulate Leave Application API
    return {
        "response": (
            f"{state['leave_type']} leave request "
            f"created successfully."
        )
    }


def reject_message(state: LeaveState):

    return {
        "response": (
            "Leave request rejected due to insufficient "
            "leave balance."
        )
    }


def approval_rejected(state: LeaveState):

    return {
        "response": "Manager rejected your leave request."
    }


# -----------------------------------
# 8. Build graph
# -----------------------------------

graph = StateGraph(LeaveState)

graph.add_node("get_leave_balance", get_leave_balance)
graph.add_node("get_leave_type", get_leave_type)
graph.add_node("check_eligibility", check_leave_eligibility)
graph.add_node("get_manager_approval", get_manager_approval)

graph.add_node("create_leave_request", create_leave_request)
graph.add_node("reject_message", reject_message)
graph.add_node("approval_rejected", approval_rejected)


# Parallel execution
graph.add_edge(START, "get_leave_balance")
graph.add_edge(START, "get_leave_type")

# Wait for both parallel nodes
graph.add_edge(
    ["get_leave_balance", "get_leave_type"],
    "check_eligibility"
)

# Eligibility routing
graph.add_conditional_edges(
    "check_eligibility",
    route_eligibility,
    {
        "eligible": "get_manager_approval",
        "insufficient": "reject_message"
    }
)

# Manager approval routing
graph.add_conditional_edges(
    "get_manager_approval",
    route_approval,
    {
        "approved": "create_leave_request",
        "rejected": "approval_rejected"
    }
)


# End nodes
graph.add_edge("create_leave_request", END)
graph.add_edge("reject_message", END)
graph.add_edge("approval_rejected", END)


# -----------------------------------
# 9. Compile workflow
# -----------------------------------

workflow = graph.compile()


# -----------------------------------
# 10. Execute workflow
# -----------------------------------

result = workflow.invoke({
    "emp_id": "12345",
    "query": "I want five days of annual leave.",
    "requested_days": 5
})

print("\nFinal Response:")
print(result["response"])
