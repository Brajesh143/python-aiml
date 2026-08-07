import ollama

response = ollama.generate(
    model="llama3:8b",
    prompt="What is the meaning of life?",
    stream=True,
)

for chunk in response:
    print(chunk['response'], end="")

print("###\n")