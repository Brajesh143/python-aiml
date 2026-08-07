from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3:8b", system="You are a storyteller.")

response = llm.invoke("Tell me the story of Bhangardh fort, Arwal, Rajasthan")

print(response.content)