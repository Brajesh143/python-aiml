from langchain_ollama import ChatOllama
from langchain.tools import tool
from langgraph.graph import START, END, StateGraph, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition

llm = ChatOllama(
    model="qwen3:0.6b",
    temperature=0
)

employees = {
    101: {
        "name": "Rahul",
        "salary": 50000,
        "department": "Engineering"
    },
    102: {
        "name": "Priya",
        "salary": 70000,
        "department": "HR"
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


tools = [get_employee_details, get_employee_salary, get_employee_department]

tool_with_llm = llm.bind_tools(tools)

tool_node = ToolNode(tools)

def chatbot(state: MessagesState):
    response = tool_with_llm.invoke(state["messages"])

    return {"messages": [response]}

graph = StateGraph(MessagesState)

graph.add_node("chatbot", chatbot)
graph.add_node("tools", tool_node)

graph.add_edge(START, "chatbot")
graph.add_conditional_edges(
    "chatbot",
    tools_condition
)

graph.add_edge("tools", "chatbot")

workflow = graph.compile()

result = workflow.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Get details of employee 101"
        }
    ]
})

print(result["messages"][-1].content)

