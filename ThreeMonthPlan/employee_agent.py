from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

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

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
        You are an Employee Information Assistant.
        You can provide details about employees, including their department and salary.
        Use the tools to fetch employee information based on their ID.
        Never invent employee information."""
)

class AgentState(TypedDict):
    question: str
    answer: str

def fetch_employee_details(state: AgentState) -> AgentState:
    question = state['question']
    answer = agent.invoke({
        "messages": [
            HumanMessage(content=question)
        ]
    })
    final_answer = answer["messages"][-1].content
    return {
        "answer": final_answer
    }

graph = StateGraph(AgentState)

graph.add_node('fetch_employee_details', fetch_employee_details)

graph.add_edge(START, 'fetch_employee_details')
graph.add_edge('fetch_employee_details', END)

workflow = graph.compile()

user_question = input("Enter your question about an employee: ")

result = workflow.invoke({"question": user_question})

print(result['answer'])
