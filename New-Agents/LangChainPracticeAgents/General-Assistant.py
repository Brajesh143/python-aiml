# Agent 1: General Assistant
# Build an assistant using:
# Prompt → Model → Parser
# Example:
# Explain Python decorators.

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="qwen3:0.6b")

template = PromptTemplate(
    template="Explain {topic} in simple language with an example.",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = template | model | parser

result = chain.invoke({"topic": "Python decorators"})

print(result)