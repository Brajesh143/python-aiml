from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# 1. Define shared state
class MedicalState(TypedDict, total=False):
    user_id: str
    symptoms: list
    user_question: str

    patient_information: dict
    medical_knowledge: dict

    disease_analysis: dict
    recommended_tests: list
    medicine_information: list

    safety_review: dict
    final_response: str


# 2. Define nodes

def patient_agent(state: MedicalState):
    # Fetch patient information from database/API
    patient_data = {
        "age": 35,
        "allergies": ["Penicillin"]
    }

    return {
        "patient_information": patient_data
    }


def medical_rag(state: MedicalState):
    # Retrieve relevant medical documents
    knowledge = {
        "possible_conditions": [
            "Viral infection",
            "Influenza"
        ]
    }

    return {
        "medical_knowledge": knowledge
    }


def disease_agent(state: MedicalState):
    # Analyze symptoms and patient context
    return {
        "disease_analysis": {
            "possible_conditions": [
                "Viral infection",
                "Influenza"
            ]
        }
    }


def test_agent(state: MedicalState):
    # Identify potential tests for clinical review
    return {
        "recommended_tests": []
    }


def medicine_agent(state: MedicalState):
    # Retrieve and assess medicine safety information
    return {
        "medicine_information": []
    }


def safety_agent(state: MedicalState):
    # Perform safety validation
    return {
        "safety_review": {
            "requires_doctor_review": True
        }
    }


def final_response(state: MedicalState):
    return {
        "final_response": (
            "Your information has been prepared "
            "for clinician review."
        )
    }


# 3. Create graph
workflow = StateGraph(MedicalState)


# 4. Register nodes
workflow.add_node("patient_agent", patient_agent)
workflow.add_node("medical_rag", medical_rag)
workflow.add_node("disease_agent", disease_agent)
workflow.add_node("test_agent", test_agent)
workflow.add_node("medicine_agent", medicine_agent)
workflow.add_node("safety_agent", safety_agent)
workflow.add_node("final_response", final_response)


# 5. Define workflow

workflow.add_edge(START, "patient_agent")
workflow.add_edge(START, "medical_rag")

# Both parallel nodes converge here
workflow.add_edge("patient_agent", "disease_agent")
workflow.add_edge("medical_rag", "disease_agent")

# Parallel execution after disease analysis
workflow.add_edge("disease_agent", "test_agent")
workflow.add_edge("disease_agent", "medicine_agent")

# Wait for both outputs
workflow.add_edge("test_agent", "safety_agent")
workflow.add_edge("medicine_agent", "safety_agent")

workflow.add_edge("safety_agent", "final_response")
workflow.add_edge("final_response", END)


# 6. Compile
app = workflow.compile()

result = app.invoke({
    "user_id": "USER_101",
    "symptoms": [
        "fever",
        "headache",
        "body pain"
    ],
    "user_question": "What could be the reason?"
})

print(result["final_response"])