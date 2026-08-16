# Agent 1: Topic Explainer
# Input:
# topic = "Python decorators"
# level = "beginner"
# Output:
# Explain decorators for a beginner.

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(model="qwen3:0.6b")

prompt = PromptTemplate(
    template="Explain the {topic} for {level}",
    input_variables=["topic", "level"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({ "topic": "Python decorators", "level": "beginner" })

print(result)