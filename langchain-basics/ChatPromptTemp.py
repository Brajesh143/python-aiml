from langchain_ollama import ChatOllama
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)
from langchain_core.messages import HumanMessage, AIMessage


# --------------------------------------------------
# 1. Create the Ollama model
# --------------------------------------------------

model = ChatOllama(
    model="qwen3:0.6b",
    temperature=0.3
)


# --------------------------------------------------
# 2. Create ChatPromptTemplate
# --------------------------------------------------

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a helpful programming teacher.
        Explain programming concepts in simple language.
        Give examples whenever useful.
        """
    ),

    # This is where previous conversation will be inserted
    MessagesPlaceholder(
        variable_name="chat_history"
    ),

    # Current user question
    (
        "human",
        "{question}"
    )
])


# --------------------------------------------------
# 3. Create conversation history
# --------------------------------------------------

chat_history = [
    HumanMessage(
        content="What is Python?"
    ),

    AIMessage(
        content="Python is a high-level, general-purpose programming language."
    ),

    HumanMessage(
        content="What can I use it for?"
    ),

    AIMessage(
        content=(
            "Python can be used for web development, "
            "automation, data science, machine learning, and AI."
        )
    )
]


# --------------------------------------------------
# 4. Create the chain
# --------------------------------------------------

chain = prompt | model


# --------------------------------------------------
# 5. Send the current question
# --------------------------------------------------

question = "Which Python library is commonly used for building AI applications?"


response = chain.invoke({
    "chat_history": chat_history,
    "question": question
})


# --------------------------------------------------
# 6. Print the response
# --------------------------------------------------

print("AI:")
print(response.content)