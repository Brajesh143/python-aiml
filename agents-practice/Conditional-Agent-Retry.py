from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_core.tools import tool


# =========================================================
# 1. State
# =========================================================

class RetryState(TypedDict):
    question: str
    attempts: int
    max_retries: int
    success: bool
    result: str


# =========================================================
# 2. Simulated failing tool
# =========================================================

@tool
def get_employee_salary(employee_name: str) -> str:
    """
    Get employee salary.

    This tool is intentionally designed to fail
    for demonstration purposes.
    """

    # Simulate failure
    raise Exception("Database connection failed")


# =========================================================
# 3. Tool Node
# =========================================================

def tool_node(state: RetryState):

    attempts = state["attempts"] + 1

    try:

        result = get_employee_salary.invoke({
            "employee_name": "Rahul"
        })

        return {
            "attempts": attempts,
            "success": True,
            "result": result
        }

    except Exception as e:

        print(f"Tool attempt {attempts} failed: {e}")

        return {
            "attempts": attempts,
            "success": False,
            "result": str(e)
        }


# =========================================================
# 4. Retry Router
# =========================================================

def retry_router(state: RetryState):

    # Tool succeeded
    if state["success"]:
        return "success"

    # Still allowed to retry
    if state["attempts"] <= state["max_retries"]:
        return "retry"

    # Retry limit reached
    return "fallback"


# =========================================================
# 5. Fallback Node
# =========================================================

def fallback_node(state: RetryState):

    return {
        "result": (
            "Sorry, we are unable to retrieve the employee "
            "information right now. Please try again later."
        )
    }


# =========================================================
# 6. Create Graph
# =========================================================

graph = StateGraph(RetryState)

graph.add_node("tool", tool_node)
graph.add_node("fallback", fallback_node)


# =========================================================
# 7. Start → Tool
# =========================================================

graph.add_edge(START, "tool")


# =========================================================
# 8. Conditional Retry
# =========================================================

graph.add_conditional_edges(
    "tool",
    retry_router,
    {
        "success": END,
        "retry": "tool",
        "fallback": "fallback"
    }
)


# =========================================================
# 9. Fallback → END
# =========================================================

graph.add_edge("fallback", END)


# =========================================================
# 10. Compile
# =========================================================

workflow = graph.compile()


# =========================================================
# 11. Execute
# =========================================================

initial_state = {
    "question": "What is Rahul's salary?",
    "attempts": 0,
    "max_retries": 2,
    "success": False,
    "result": ""
}

result = workflow.invoke(initial_state)

print("\nFinal Result:")
print(result["result"])

print("\nTotal attempts:")
print(result["attempts"])