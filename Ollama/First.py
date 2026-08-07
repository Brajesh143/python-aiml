# Generate function example

import ollama

response = ollama.generate(
    model="llama3.2:1b",
    prompt="What is the capital of France?",
    stream=True,
)

for chunk in response:
    print(chunk['response'], end='')

