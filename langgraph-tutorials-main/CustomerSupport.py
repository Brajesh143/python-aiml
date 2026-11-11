from langgraph.graph import StateGraph, START, END
from typing import Literal, TypedDict, Optional
from langchain_ollama import ChatOllama
from pydantic import BaseModel

llm = ChatOllama(model="qwen3:0.6b", temperature=0)

class RouteDecision(BaseModel):
    intent: Literal[
        "order_tracking",
        "cancel_order",
        "return_process",
        "return_order",
        "refund_policy",
        "refund_status",
        "payment_issue",
        "general_support"
    ]

    action_type: Literal[
        "information",
        "execute",
        "investigate",
        "escalate"
    ]

    order_id: Optional[str] = None
    requires_confirmation: bool = False


class SupportState(TypedDict):
    question: str
    intent: str
    action_type: str
    order_id: Optional[str]
    requires_confirmation: bool
    result: Optional[dict]
    final_response: Optional[str]


def generate_response(state: SupportState) -> SupportState:
    query = state['question']
    response = llm.invoke(query)
    return {'question': query, 'response': response}

def router_node(state: SupportState):

    decision = llm.with_structured_output(
        RouteDecision
    ).invoke(state["question"])

    return {
        "intent": decision.intent,
        "action_type": decision.action_type
    }

def route_request(state: SupportState):

    intent = state["intent"]

    if intent in ["order_tracking", "cancel_order",
                  "return_order"]:
        return "order_workflow"

    elif intent in ["return_process", "refund_policy"]:
        return "policy_workflow"

    elif intent in ["refund_status", "payment_issue"]:
        return "payment_workflow"

    return "support_workflow"

def order_workflow(state: SupportState):
    intent = state["intent"]
    order_id = state.get("order_id")

    if intent == "order_tracking":
        result = {
            "status": "success",
            "message": f"Your order {order_id or 'ORD-1001'} is currently in transit.",
            "estimated_delivery": "2026-11-10"
        }

    elif intent == "cancel_order":
        result = {
            "status": "success",
            "message": f"Order {order_id or 'ORD-1001'} cancellation request received.",
            "action": "cancellation_requested"
        }

    elif intent == "return_order":
        result = {
            "status": "success",
            "message": f"Return request initiated for order {order_id or 'ORD-1001'}.",
            "action": "return_initiated"
        }

    else:
        result = {
            "status": "error",
            "message": "Unsupported order operation."
        }

    return {"result": result}


def policy_workflow(state: SupportState):
    intent = state["intent"]

    if intent == "return_process":
        result = {
            "status": "success",
            "policy": "Items can be returned within 7 days of delivery.",
            "instructions": [
                "Open your orders section.",
                "Select the item.",
                "Click on Initiate Return.",
                "Select the reason for return."
            ]
        }

    elif intent == "refund_policy":
        result = {
            "status": "success",
            "policy": "Refunds are processed within 5-7 business days after approval.",
            "refund_method": "Original payment method"
        }

    else:
        result = {
            "status": "error",
            "message": "Policy information not available."
        }

    return {"result": result}


def payment_workflow(state: SupportState):
    intent = state["intent"]
    order_id = state.get("order_id")

    if intent == "refund_status":
        result = {
            "status": "success",
            "order_id": order_id or "ORD-1001",
            "refund_status": "processing",
            "message": "Your refund is currently being processed.",
            "expected_time": "5-7 business days"
        }

    elif intent == "payment_issue":
        result = {
            "status": "investigation_required",
            "message": "We have received your payment issue.",
            "action": "payment_investigation_created",
            "ticket_id": "PAY-2026-001"
        }

    else:
        result = {
            "status": "error",
            "message": "Unsupported payment operation."
        }

    return {"result": result}


def support_workflow(state: SupportState):
    return {
        "result": {
            "status": "success",
            "message": "Your query has been forwarded to general customer support.",
            "ticket_id": "SUP-2026-001",
            "action": "support_ticket_created"
        }
    }

def response_node(state: SupportState):

    prompt = f"""
    You are a professional customer support assistant.

    Customer Query: {state['question']}

    Detected Intent: {state['intent']}

    Workflow Result: {state.get('result')}

    Generate a clear, friendly response for the customer.
    Do not invent any information.
    """

    response = llm.invoke(prompt)

    return {
        "final_response": response.content
    }


graph = StateGraph(SupportState)

graph.add_node("router", router_node)
graph.add_node("order_workflow", order_workflow)
graph.add_node("policy_workflow", policy_workflow)
graph.add_node("payment_workflow", payment_workflow)
graph.add_node("support_workflow", support_workflow)
graph.add_node("response", response_node)

graph.add_edge(START, "router")
graph.add_conditional_edges(
    "router",
    route_request,
    {
        "order_workflow": "order_workflow",
        "policy_workflow": "policy_workflow",
        "payment_workflow": "payment_workflow",
        "support_workflow": "support_workflow"
    }
)
graph.add_edge("order_workflow", "response")
graph.add_edge("policy_workflow", "response")
graph.add_edge("payment_workflow", "response")
graph.add_edge("support_workflow", "response")
graph.add_edge("response", END)

workflow = graph.compile()

# graph_image = workflow.get_graph()

# Print Mermaid diagram
# print(graph_image.draw_mermaid())

query = input("Enter your customer support query: ")
result = workflow.invoke({
    "question": query
})

print("\nCustomer Support Response:")
print(result["final_response"])