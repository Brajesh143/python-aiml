# Use your existing Ollama model and ask it the same question with different prompts. Observe how the responses change.

import ollama

prompt1 = "What is Artificial Intelligence? What are the main components of AI?"
response1 = ollama.generate(
    model='qwen3:0.6b',
    prompt=prompt1
)


prompt2 = "Explain the concept of Artificial Intelligence in simple terms for a 10-year-old. What are the main components of AI?"
response2 = ollama.generate(
    model='qwen3:0.6b',
    prompt=prompt2
)
print("Response to prompt 1:", response1['response'])
print("Response to prompt 2:", response2['response'])