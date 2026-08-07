from langchain_ollama import ChatOllama
import streamlit as st

model = ChatOllama(model="qwen3:0.6b")

st.title("Chatbot Interface")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input()
st.session_state.chat_history.append({"role": "user", "content": user_input})
if st.button("Send"):
    if user_input:
        response = model.invoke([{"role": "user", "content": user_input}])
        st.session_state.chat_history.append({"role": "assistant", "content": response.content})

for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.write(f"You: {message['content']}")
    else:
        st.write(f"Assistant: {message['content']}")
