from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


model = ChatOllama(model="qwen3:0.6b")

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(f"Assistant: {response.content}")

