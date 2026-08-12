from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(
    model="qwen3:0.6b",
    temperature=0.3
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert Python teacher. "
        "Explain concepts clearly for beginners."
    ),
    (
        "human",
        "Explain {topic} with a simple example."
    )
])

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({
    "topic": "generators"
})

print(result)