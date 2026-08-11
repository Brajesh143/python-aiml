from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model="qwen3:0.6b")

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt | model | parser

user_input = input("Enter a topic: \n")

result = chain.invoke({ 'topic': user_input })

print(result)