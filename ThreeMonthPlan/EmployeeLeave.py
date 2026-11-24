from typing import TypedDict

from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

from langchain.agents import create_agent
from langgraph.graph import StateGraph, START, END
# from langchain_google_genai import ChatGoogleGenerativeAI
# import os

# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     google_api_key=os.getenv("GEMINI_API_KEY"),
#     temperature=0
# )

# ----------------------------------
# 1. Initialize LLM
# ----------------------------------

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
)


# ----------------------------------
# 2. Employee database (sample data)
# ----------------------------------

EMPLOYEES = {
    101: {
        "name": "Rahul",
        "annual_leaves": 20,
        "remaining_leaves": 12
    },
    102: {
        "name": "Amit",
        "annual_leaves": 20,
        "remaining_leaves": 8
    }
}


# ----------------------------------
# 3. Leave balance tool
# ----------------------------------

@tool
def get_leave_balance(employee_id: int) -> str:
    """Get the remaining annual leave balance for an employee."""

    employee = EMPLOYEES.get(employee_id)

    if employee is None:
        return "Employee not found."

    return (
        f"Employee: {employee['name']}\n"
        f"Annual leaves: {employee['annual_leaves']}\n"
        f"Remaining leaves: {employee['remaining_leaves']}"
    )


# ----------------------------------
# 4. HR policy tool
# ----------------------------------

@tool
def search_leave_policy(query: str) -> str:
    """Search HR policy documents for applicable leave rules."""

    return """
    Annual Leave Policy:
    1. Employees receive 20 annual leaves per year.
    2. Leave requests require manager approval.
    3. Employees should submit leave requests in advance.
    """

# ----------------------------------
# 5. Policy Agent
# ----------------------------------

policy_agent = create_agent(
    model=llm,
    tools=[search_leave_policy],
    system_prompt="""
    You are an HR Policy Assistant.

    Your responsibility is to explain the
    applicable annual leave policy.

    Use the search_leave_policy tool to
    retrieve the policy.

    Do not invent policy rules.
    """
)


# ----------------------------------
# 6. Leave Balance Agent
# ----------------------------------

balance_agent = create_agent(
    model=llm,
    tools=[get_leave_balance],
    system_prompt="""
    You are an Employee Leave Balance Assistant.

    Your responsibility is to retrieve the
    employee's remaining annual leave balance.

    Always use the get_leave_balance tool.

    Do not invent employee information.
    """
)

class LeaveState(TypedDict):
    employee_id: int
    question: str
    policy_result: str
    balance_result: str
    final_answer: str

# ----------------------------------
# 7. Policy Agent Node
# ----------------------------------

def policy_node(state: LeaveState):

    response = policy_agent.invoke({
        "messages": [
            HumanMessage(
                content=(
                    "Explain the applicable annual "
                    "leave policy for this employee."
                )
            )
        ]
    })

    policy_result = response["messages"][-1].content

    return {
        "policy_result": policy_result
    }


# ----------------------------------
# 8. Balance Agent Node
# ----------------------------------

def balance_node(state: LeaveState):

    response = balance_agent.invoke({
        "messages": [
            HumanMessage(
                content=(
                    f"Find the remaining annual leaves "
                    f"for employee ID {state['employee_id']}."
                )
            )
        ]
    })

    balance_result = response["messages"][-1].content

    return {
        "balance_result": balance_result
    }


# ----------------------------------
# 9. Final Response Node
# ----------------------------------

def final_response_node(state: LeaveState):

    final_answer = f"""
    Your remaining leave balance:

    {state['balance_result']}

    Applicable leave policy:

    {state['policy_result']}
    """

    return {
        "final_answer": final_answer
    }

# ----------------------------------
# 10. Build Parent Graph
# ----------------------------------

builder = StateGraph(LeaveState)

builder.add_node("policy", policy_node)
builder.add_node("balance", balance_node)
builder.add_node("final_response", final_response_node)

# Define the execution sequence
builder.add_edge(START, "policy")
builder.add_edge("policy", "balance")
builder.add_edge("balance", "final_response")
builder.add_edge("final_response", END)

# Compile the graph
leave_graph = builder.compile()

# ----------------------------------
# 11. Invoke Parent Graph
# ----------------------------------

result = leave_graph.invoke({
    "employee_id": 101,
    "question": (
        "Find my remaining leaves and explain "
        "the applicable leave policy."
    ),
    "policy_result": "",
    "balance_result": "",
    "final_answer": ""
})

print(result["final_answer"])