import ollama

response = ollama.generate(
    model="qwen3:0.6b",
    prompt="Write a three-month plan for learning Python programming, including weekly goals and resources."
)

print(response['response'])
