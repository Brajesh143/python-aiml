from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.agents import create_agent
from langchain.tools import tool

model = ChatOllama(model="qwen3:8b")

# Tool Creation

employees = {
    "rahul": {
        "role": "Backend Developer",
        "experience": 5,
        "department": "Engineering"
    },
    "priya": {
        "role": "Frontend Developer",
        "experience": 4,
        "department": "Engineering"
    },
    "amit": {
        "role": "DevOps Engineer",
        "experience": 6,
        "department": "Infrastructure"
    }
}

@tool
def get_employee_info(employee_name: str) -> str:
    """Get information about an employee using their name."""

    employee_info = employees.get(employee_name.lower().strip())

    if not employee_info:

        return f"Employee {employee_name} not available in the list"

    return (
        f"Name: {employee_name}\n"
        f"Role: {employee_info['role']}\n"
        f"Experience: {employee_info['experience']} years\n"
        f"Department: {employee_info['department']}"
    )

tools = [get_employee_info]

agent = create_agent(
    model=model,
    tools=tools
)

# result = agent.invoke({
#     "messages": [
#         {
#             "role": "user",
#             "content": "What is Rahul's role?"
#         }
#     ]
# })

result = agent.invoke({
    "messages": [HumanMessage("What is Rahul's role?")]
})

print(result["messages"][-1].content)

print("-------- \n", result["messages"])


