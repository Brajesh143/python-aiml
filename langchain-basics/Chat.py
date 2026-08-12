from langchain_ollama import ChatOllama
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)
from langchain_core.messages import HumanMessage, AIMessage


model = ChatOllama(
    model="qwen3:0.6b",
    temperature=0.3
)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful AI assistant."
    ),
    MessagesPlaceholder(
        variable_name="chat_history"
    ),
    (
        "human",
        "{question}"
    )
])


chain = prompt | model


chat_history = []


# -------------------------------
# First question
# -------------------------------

question = "What is LangChain?"

response = chain.invoke({
    "chat_history": chat_history,
    "question": question
})

print("User:", question)
print("AI:", response.content)


# Save the conversation
chat_history.append(
    HumanMessage(content=question)
)

chat_history.append(
    AIMessage(content=response.content)
)


# -------------------------------
# Second question
# -------------------------------

question = "What is it mainly used for?"

response = chain.invoke({
    "chat_history": chat_history,
    "question": question
})

print("\nUser:", question)
print("AI:", response.content)


# Save second conversation
chat_history.append(
    HumanMessage(content=question)
)

chat_history.append(
    AIMessage(content=response.content)
)


# -------------------------------
# Third question
# -------------------------------

question = "Can I use it with Ollama?"

response = chain.invoke({
    "chat_history": chat_history,
    "question": question
})

print("\nUser:", question)
print("AI:", response.content)