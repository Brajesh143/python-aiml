# Agent 2: Technical Answer Agent
# Prompt:
# Explain Node.js event loop.
# Experiment with:
# temperature
# top_k
# top_p

# Focus: Model behavior and sampling.

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(
    model="qwen3:0.6b",
    temperature=0.3,
    top_k=2,
    top_p=0.5
)

template = PromptTemplate(
    template="Explain {technology} {topic}.",
    input_variables=["technology", "topic"]
)

parser = StrOutputParser()

chain = template | model | parser

result = chain.invoke({"technology": "Node.js", "topic": "Event Loop"})

print(result)