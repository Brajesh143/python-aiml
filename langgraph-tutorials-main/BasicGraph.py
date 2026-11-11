# Scenario 1: User age verification
# Requirements:
# 1. Accept user's name and age.
# 2. Validate the age.
# 3. If age is below 18, reject registration.
# 4. If age is 18 or above, allow registration.
# 5. Generate an appropriate response.

from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from pydantic import BaseModel

class AgeVerificationState(TypedDict):
    name: str
    age: int
    is_eligible: bool
    response: str

graph = StateGraph(AgeVerificationState)

def age_verification(state: AgeVerificationState):
    age = state["age"]
    is_eligible = age >= 18
    return {
        "is_eligible": is_eligible
    }

def route_age(state: AgeVerificationState):
    if state["is_eligible"]:
        return "eligible"
    else:
        return "not_eligible"

def reject_registration(state: AgeVerificationState):
    name = state["name"]
    return {
        "response": f"Sorry {name}, you are not eligible to register as you are under 18."
    }

def allow_registration(state: AgeVerificationState):
    name = state["name"]
    return {
        "response": f"Congratulations {name}, you are eligible to register!"
    }

graph.add_node('age_verification', age_verification)
graph.add_node('reject_registration', reject_registration)
graph.add_node('allow_registration', allow_registration)

graph.add_edge(START, 'age_verification')
graph.add_conditional_edges('age_verification', route_age, {
    "eligible": "allow_registration",
    "not_eligible": "reject_registration"
})
graph.add_edge('allow_registration', END)
graph.add_edge('reject_registration', END)

workflow = graph.compile()

result = workflow.invoke({
    "name": input("Enter your name: "),
    "age": int(input("Enter your age: "))
})

print(result["response"])

