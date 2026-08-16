from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode
from typing import Literal


# =========================================================
# 1. Model
# =========================================================

model = ChatOllama(
    model="qwen3:8b",
    temperature=0
)


# =========================================================
# 2. Employee Data
# =========================================================

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


# =========================================================
# 3. Tools
# =========================================================

@tool
def get_employee_info(employee_name: str) -> str:
    """Get information about an employee using their name."""

    employee_info = employees.get(
        employee_name.lower().strip()
    )

    if not employee_info:
        return (
            f"Employee '{employee_name}' "
            "is not available in the list."
        )

    return (
        f"Name: {employee_name}\n"
        f"Role: {employee_info['role']}\n"
        f"Experience: {employee_info['experience']} years\n"
        f"Department: {employee_info['department']}"
    )


@tool
def calculate(
    operation: str,
    a: float,
    b: float
) -> float:
    """Perform a mathematical operation on two numbers."""

    operation = operation.lower().strip()

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero.")

        return a / b

    else:
        raise ValueError(
            "Supported operations are: "
            "add, subtract, multiply, divide."
        )


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
        city.lower().strip(),
        f"Weather data for {city} is not available."
    )


tools = [
    get_employee_info,
    calculate,
    get_weather
]


# =========================================================
# 4. Bind tools to model
# =========================================================

model_with_tools = model.bind_tools(tools)


# =========================================================
# 5. Agent node
# =========================================================

def agent_node(state: MessagesState):
    """
    Ask the LLM what to do next.
    """

    response = model_with_tools.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


# =========================================================
# 6. Tool node
# =========================================================

tool_node = ToolNode(tools)


# =========================================================
# 7. Routing function
# =========================================================

def should_continue(
    state: MessagesState
) -> Literal["tools", END]:

    last_message = state["messages"][-1]

    # If LLM requested a tool
    if last_message.tool_calls:
        return "tools"

    # Otherwise, final answer
    return END


# =========================================================
# 8. Create LangGraph
# =========================================================

graph = StateGraph(MessagesState)


# Add nodes
graph.add_node("agent", agent_node)
graph.add_node("tools", tool_node)


# START → agent
graph.add_edge(START, "agent")


# agent → tools OR END
graph.add_conditional_edges(
    "agent",
    should_continue
)


# tools → agent
graph.add_edge("tools", "agent")


# =========================================================
# 9. Compile graph
# =========================================================

app = graph.compile()


# =========================================================
# 10. Run the graph
# =========================================================

result = app.invoke({
    "messages": [
        HumanMessage(
            content="What is the add of 20 and 35?"
        )
    ]
})


# =========================================================
# 11. Print results
# =========================================================

print("Final Answer:")
print(result["messages"][-1].content)

print("\n====================")

print("All Messages:")
for message in result["messages"]:
    print(message)
    print("--------------------")