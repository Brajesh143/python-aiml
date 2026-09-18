from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langchain_core.tools import tool
from typing import TypedDict

LLM_MODEL = "qwen3:0.6b"

llm = ChatOllama(model=LLM_MODEL)

tickets = {
    "T1001": "Open",
    "T1002": "Resolved",
    "T1003": "In Progress"
}

users = {
    "rahul@gmail.com": {
        "name": "Rahul",
        "department": "Engineering"
    },
    "priya@gmail.com": {
        "name": "Priya",
        "department": "HR"
    }
}

orders = {
    "ORD101": "Shipped",
    "ORD102": "Delivered",
    "ORD103": "Processing"
}

@tool
def get_ticket_status_tool(ticket_id: str):
    "Get the ticket status "

class TicketState(TypedDict):
    question: str
    result: str

def route(state: TicketState):
    question = state["question"].lower()

    if "ticket" in question:
        return "ticket"

    elif "user" in question:
        return "user"

    else:
        return "order"



def get_ticket_status(state: TicketState):
    key = state["key"]

    result = tickets[key]

    return {
        "result": result
    }

def get_user_info(state: TicketState):
    key = state["key"]
    
    result = users[key]

    return {
        "result": result
    }


def get_order_status(state: TicketState):
    key = state["key"]
        
    result = orders[key]

    return {
        "result": result
    }


graph = StateGraph(TicketState)

graph.add_node('get_ticket_status', get_ticket_status)
graph.add_node('get_user_info', get_user_info)
graph.add_node('get_order_status', get_order_status)

graph.add_conditional_edges(START, route, {
    "ticket": "get_ticket_status",
    "user": "get_user_info",
    "order": "get_order_status"
})

graph.add_edge("get_ticket_status", END)
graph.add_edge("get_user_info", END)
graph.add_edge("get_order_status", END)

workflow = graph.compile()

initial_state = {
    "question": "What is the status of ticket T1001?"
}

result = workflow.invoke(initial_state)

print(result["result"])