from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model="qwen3:0.6b")

prompt = PromptTemplate(
    template="You are a storyteller. Tell me the story on {topic}.",
    input_variables=["topic"]
)

response = model.invoke(prompt.format(topic="Bhangardh fort, Arwal, Rajasthan"))
print(response.content)