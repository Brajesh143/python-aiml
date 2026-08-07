from langchain_ollama import ChatOllama
import streamlit as st

model = ChatOllama(model="qwen3:0.6b", temperature=0.7)

st.header("Chat with Ollama Model")

user_input = st.text_input("You: ", "")

if st.button("Send"):
    model_response = model.invoke(user_input)
    st.write("Ollama: ", model_response.content)