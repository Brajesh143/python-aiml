from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from typing import TypedDict

# State Creation
class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int

    sr: float
    bpb: float
    boundary_percent: float
    summary: str

def cal_st(state: BatsmanState):

    sr = (state['runs']/state['balls'])*100
    
    return {'sr': sr}

def cal_bpb(state: BatsmanState):

    bpb = state['balls']/(state['fours'] + state['sixes'])

    return {'bpb': bpb}

def cal_boundary_percent(state: BatsmanState):

    boundary_percent = (((state['fours'] * 4) + (state['sixes'] * 6))/state['runs'])*100

    return {'boundary_percent': boundary_percent}

def summary(state: BatsmanState):

    summary = f"""
    Strike Rate - {state['sr']} \n
    Balls per boundary - {state['bpb']} \n
    Boundary percent - {state['boundary_percent']}
    """
    
    return {'summary': summary}

# Graph Initialization
graph = StateGraph(BatsmanState)

graph.add_node('cal_sr', cal_st)
graph.add_node('cal_bpb', cal_bpb)
graph.add_node('cal_boundary_percent', cal_boundary_percent)
graph.add_node('summary', summary)

# Create Edges
graph.add_edge(START, 'cal_sr')
graph.add_edge(START, 'cal_bpb')
graph.add_edge(START, 'cal_boundary_percent')
graph.add_edge('cal_sr', 'summary')
graph.add_edge('cal_bpb', 'summary')
graph.add_edge('cal_boundary_percent', 'summary')
graph.add_edge('summary', END)

workflow = graph.compile()

intial_state = {
    'runs': 100,
    'balls': 50,
    'fours': 6,
    'sixes': 4
}

result = workflow.invoke(intial_state)

print(result)



