from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.tools import tool
from langchain.agents import create_agent

# model initialization
model = ChatOllama(model="qwen3:8b")

# Employee Data

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

# Tool Creation

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

@tool
def calculate(operation: str, a: float, b: float) -> float:
    """Perform a mathematical operation on two numbers."""

    if operation == 'add':
        return a + b

    elif operation == 'subtract':
        return a -b

    elif operation == 'multiply':
        return a * b

    elif operation == 'divide':
        if b == 0:
            raise ValueError("Can not divided by zero")
        return a / b

    else:
        raise ValueError("Unsupported operation, We are supporting only add, subtract, multiply and divide")

@tool
def get_weather(city: str) -> str:
    """Get the weather for a city."""
    
    weather_data = {
        "delhi": "Hot and sunny, 38°C",
        "mumbai": "Humid and cloudy, 31°C",
        "bangalore": "Pleasant and cloudy, 24°C",
        "pune": "Partly cloudy, 27°C"
    }

    return weather_data.get(
        city.lower(),
        f"Weather data for {city} is not available."
    )

tools = [get_employee_info, calculate, get_weather]

agent = create_agent(
    model=model,
    tools=tools
)

result = agent.invoke({
    "messages": [HumanMessage("What is the add of 20 and 35?")]
})

print(result["messages"][-1].content)

print("========== \n")
print(result["messages"])

print("========== \n")
print(result["messages"][-1])