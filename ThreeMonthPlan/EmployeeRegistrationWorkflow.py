from typing import TypedDict
from langgraph.graph import START, END, StateGraph
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

llm = ChatOllama(
    model="qwen3:0.6b",
    temperature=0
)

class RegistrationState(TypedDict):
    name: str
    age: int
    is_age_verify: bool
    response: str

graph = StateGraph(RegistrationState)

def age_verify(state: RegistrationState) -> dict:
    """Check whether the applicant meets the minimum age."""
    return {
        "is_age_verify": state["age"] >= 18
    }

def register(state: RegistrationState) -> dict:
    return {
        "response": (
            f"Registration successful. Welcome, {state['name']}!"
        )
    }


def reject(state: RegistrationState) -> dict:
    return {
        "response": (
            f"Sorry, {state['name']}. You must be at least 18 "
            "years old to register."
        )
    }

def router(state: RegistrationState) -> str:
    """Return the name of the next node."""
    if state["is_age_verify"]:
        return "register"

    return "reject"

graph.add_node("age_verify", age_verify)
graph.add_node("register", register)
graph.add_node("reject", reject)

graph.add_edge(START, "age_verify")
graph.add_conditional_edges("age_verify", router, {
    "register": "register",
    "reject": "reject"
})

graph.add_edge("register", END)
graph.add_edge("reject", END)

workflow = graph.compile()

result = workflow.invoke({
    "name": "Ronny",
    "age": 10,
    "is_age_verify": False,
    "response": "",
})

print(result["response"])

