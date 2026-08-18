# Agent 2: Interview Question Generator
# Input:
# technology = "Node.js"
# experience = "senior"
# count = 5
# Output:
# Generate 5 senior-level Node.js questions.

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(model="qwen3:0.6b")

template = PromptTemplate(
    template="Generate {count} {experience} level {technology} questions.",
    input_variables=["count", "experience", "technology"]
)

parser = StrOutputParser()

chain = template | model | parser

result = chain.invoke({ "count": 8, "experience": "senior", "technology": "React.js" })

print(result)