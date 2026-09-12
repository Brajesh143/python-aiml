from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

model = ChatOllama(model="qwen3:0.6b")

class InputState(TypedDict):
    question: str
    answer: str

def get_answer(state: InputState) -> InputState:
    question = state['question']

    prompt = f'Answer the following question {question}'

    answer = model.invoke(prompt).content
    
    # update the answer in the state
    state['answer'] = answer

    return state

graph = StateGraph(InputState)

graph.add_node('get_answer', get_answer)

graph.add_edge(START, 'get_answer')
graph.add_edge('get_answer', END)

workflow = graph.compile()    

# execute
intial_state = {'question': 'Who is the PrimeMinister of India?'}

final_state = workflow.invoke(intial_state)

print(final_state['answer'])
