# Scenario 2: Student examination result

# Business scenario: Build an AI-powered student result evaluation workflow.

# Requirements:
# 1. Accept student name and marks.
# 2. Calculate the percentage.
# 3. If marks are below 40%, mark the student as failed.
# 4. If marks are between 40% and 74%, assign Grade B.
# 5. If marks are 75% or above, assign Grade A.
# 6. Generate a result message.


from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class StudentResultState(TypedDict):
    name: str
    marks: float
    percentage: float
    grade: str
    result_message: str

def calculate_percentage(state: StudentResultState):
    marks = state["marks"]
    percentage = marks  # Assuming marks are already in percentage format
    return {
        "percentage": percentage
    }

def check_percentage(state: StudentResultState):
    percentage = state["percentage"]
    if percentage < 40:
        return "assign_fail"
    else:
        return "assign_grade"

def assign_grade(state: StudentResultState):
    percentage = state["percentage"]
    if percentage >= 75:
        grade = "A"
    else:
        grade = "B"
    return {
        "grade": grade
    }

def assign_fail(state: StudentResultState):
    return {
        "grade": "Fail"
    }

def generate_result_message(state: StudentResultState):
    name = state["name"]
    grade = state["grade"]
    if grade == "Fail":
        result_message = f"Sorry {name}, you have failed the examination."
    else:
        result_message = f"Congratulations {name}, you have passed with Grade {grade}."
    return {
        "result_message": result_message
    }


graph = StateGraph(StudentResultState)

graph.add_node('calculate_percentage', calculate_percentage)
graph.add_node('assign_grade', assign_grade)
graph.add_node('assign_fail', assign_fail)
graph.add_node('generate_result_message', generate_result_message)

graph.add_edge(START, 'calculate_percentage')
graph.add_conditional_edges('calculate_percentage', check_percentage, {
    "assign_grade": 'assign_grade',
    "assign_fail": 'assign_fail'
})

graph.add_edge('assign_grade', 'generate_result_message')
graph.add_edge('assign_fail', 'generate_result_message')
graph.add_edge('generate_result_message', END)

workflow = graph.compile()

result = workflow.invoke({
    "name": input("Enter student name: "),
    "marks": float(input("Enter marks (0-100): "))
})

print(result["result_message"])

