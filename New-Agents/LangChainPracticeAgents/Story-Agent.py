# Agent 1: Creative Story Agent
#       Prompt:
#       Create a short story about an AI engineer.
#       Experiment with:
#       temperature=0
#       temperature=0.5
#       temperature=1

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

template = PromptTemplate(
    template="Create a short story about {topic}.",
    input_variables=["topic"]
)

parser = StrOutputParser()

for temperature in [0, 0.5, 1.0]:
    model = ChatOllama(
        model="qwen3:0.6b",
        temperature=temperature
    )

    chain = template | model | parser

    result = chain.invoke({"topic": "AI engineer"})

    print(result)
