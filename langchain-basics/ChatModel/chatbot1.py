from langchain_ollama import ChatOllama
import streamlit as st

# Load model
model = ChatOllama(
    model="qwen3:0.6b",
    temperature=0
)

st.title("🤖 Chatbot Interface")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
with st.container(height=700, border=True):
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Chat input (automatically stays at the bottom)
prompt = st.chat_input("Enter your message...")

if prompt:
    # Store user message
    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    # Get response from Ollama
    response = model.invoke(prompt)

    # Store assistant response
    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": response.content,
        }
    )

    st.rerun()