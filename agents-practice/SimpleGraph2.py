from langchain_ollama import ChatOllama
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

LLM_MODEL = "qwen3:0.6b"

llm = ChatOllama(model=LLM_MODEL)


class InputAnswer(TypedDict):
    input: str
    answer: str

def get_answer(state: InputAnswer) -> InputAnswer:
    input_data = state["input"]

    prompt = f"Please answer this question {input_data}"

    result = llm.invoke(prompt).content

    state["answer"] = result

    return state

graph = StateGraph(InputAnswer)

graph.add_node('get_answer', get_answer)

graph.add_edge(START, 'get_answer')
graph.add_edge('get_answer', END)

workflow = graph.compile()

user_input = input("What is your question? \n")

initial_state = { "input": user_input }

result = workflow.invoke(initial_state)

print(result)