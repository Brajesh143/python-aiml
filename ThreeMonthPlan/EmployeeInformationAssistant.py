from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

llm = ChatOllama(
    model="qwen3:0.6b",
    temperature=0
)

employees = [
    {
        "employee_id": "EMP001",
        "name": "Rahul Sharma",
        "department": "Engineering",
        "designation": "Senior Software Engineer",
        "joining_date": "2021-03-15"
    },
    {
        "employee_id": "EMP002",
        "name": "Priya Verma",
        "department": "Human Resources",
        "designation": "HR Manager",
        "joining_date": "2020-07-10"
    },
    {
        "employee_id": "EMP003",
        "name": "Amit Kumar",
        "department": "Engineering",
        "designation": "Backend Developer",
        "joining_date": "2022-01-20"
    },
    {
        "employee_id": "EMP004",
        "name": "Neha Singh",
        "department": "Finance",
        "designation": "Financial Analyst",
        "joining_date": "2019-11-05"
    },
    {
        "employee_id": "EMP005",
        "name": "Vikas Gupta",
        "department": "Engineering",
        "designation": "Tech Lead",
        "joining_date": "2018-06-18"
    }
]

@tool
def get_employee_details(emp_id) :
    """This tool is used to fetch the employee details by using employee_id.
        It can fetch employee_id, name, department, designation and joining_date.
    """
    employee = next(
        (emp for emp in employees
         if emp["employee_id"] == emp_id),
        None
    )

    if employee:
        return employee

    return "Employee not found"

tools = [get_employee_details]

agent = create_agent(
    llm,
    tools
)

response = agent.invoke({
    "messages": HumanMessage("What is the designation of employee of employee_id EMP003?")
})

print(response["messages"][-1].content)