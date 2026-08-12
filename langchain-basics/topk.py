from langchain_ollama import ChatOllama

prompt = "Give me an interesting idea for an AI startup."

for top_k in [1, 5, 20, 50]:
    model = ChatOllama(
        model="qwen3:0.6b",
        temperature=0.7,
        top_k=top_k
    )

    response = model.invoke(prompt)

    print(f"\n===== top_k: {top_k} =====")
    print(response.content)