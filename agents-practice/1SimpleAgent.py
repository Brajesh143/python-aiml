from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain.agents.middleware import AgentMiddleware

# model initialization
model = ChatOllama(model="qwen3:0.6b")

# Tool Creation
@tool
def get_employee_info(employee_name: str) -> str:
    """Get information about an employee using their name."""
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

    employee_info = employees.get(employee_name.lower().strip())

    if not employee_info:
        raise Exception(f"Employee {employee_name} not available in the list")

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
        return a - b

    elif operation == 'multiply':
        return a * b

    elif operation == 'divide':
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

    else:
        return f"Invalid operation: {operation}. Please use 'add', 'subtract', 'multiply', or 'divide'."

@tool
def failing_tool(message: str) -> str:
    """A tool that intentionally fails for testing error handling."""
    raise Exception(f"Tool failed intentionally: {message}")

tools = [get_employee_info, calculate, failing_tool]

class ToolCallLimitMiddleware(AgentMiddleware):

    def __init__(self, max_tool_calls=3):
        self.max_tool_calls = max_tool_calls

    def wrap_tool_call(self, request, handler):

        messages = request.state.get("messages", [])

        tool_call_count = sum(
            1
            for message in messages
            if getattr(message, "type", None) == "tool"
        )

        if tool_call_count >= self.max_tool_calls:
            raise Exception(
                f"Maximum tool call limit "
                f"of {self.max_tool_calls} reached."
            )

        return handler(request)


agent = create_agent(
    model=model,
    tools=tools,
    middleware=[
        ToolCallLimitMiddleware(max_tool_calls=3)
    ]
)

user_query = input("How may I help you? \n")

try:
    result = agent.invoke({
        "messages": HumanMessage(content=user_query)
    })

    print(result["messages"][-1].content)
except Exception as e:
    print(f"Agent failed: {e}")