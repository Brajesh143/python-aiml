from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:0.6b", system="You are a storyteller.")

response = llm.invoke("Tell me the story of Bhangardh fort, Arwal, Rajasthan")

print(response.content)