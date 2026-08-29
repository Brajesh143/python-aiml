# Exercise 1 — Temperature experiment — 15 min

# Using Ollama, ask the same question with:

# temperature = 0
# temperature = 0.5
# temperature = 1

# Use something like:

# Explain event loop in Node.js in 5 sentences.
# frequency_penalty=0.5  Purpose: Reduces repeated tokens/phrases.
# presence_penalty=0.5  Purpose: Encourages the model to use new tokens/topics rather than repeatedly relying on tokens already present.
# seed=42 Purpose: Helps make generation more reproducible.

import ollama

temps = [0, 0.3, 0.5, 0.7, 1.0]

for temp in temps:
    result = ollama.generate(
        model="qwen3:0.6b", 
        prompt="Tell me about Narendra Modi in 2 lines.",
        # max_tokens=100
        options={
            "temperature": temp,
            "max_tokens": 5
        },
        
    )

    print(f"This result is for temp {temp}. \n")
    print(result.response)
    print("\n")

# prompt1 = """
# You are a senior Node.js interviewer.
# Ask difficult interview questions.
# Do not provide the answer immediately.
# """

# prompt2 = """
# You are a beginner-friendly programming teacher.
# Explain concepts using simple examples.
# """
# response = ollama.generate(model="qwen3:0.6b", prompt=prompt2, options={"temperature": 0.7})

# print(response.response)


# prompt = """
# Brajesh is a Senior Software Engineer with 8 years
# of experience in JavaScript, Node.js and Python.
# """

# response = ollama.generate(
#     model="qwen3:0.6b",
#     prompt=prompt,
#     format={
#         "type": "object",
#         "properties": {
#             "name": {"type": "string"},
#             "role": {"type": "string"},
#             "experience": {"type": "integer"},
#             "skills": {
#                 "type": "array",
#                 "items": {
#                     "type": "string"
#                 }
#             }
#         },
#         "required": [
#             "name",
#             "role",
#             "experience",
#             "skills"
#         ]
#     }
# )

# print(response.response)

# prompt1 = "Explain RAG."

# prompt2 = "Explain RAG to a backend developer."

# prompt3 = """
# Explain RAG to a senior Node.js developer.
# Include architecture, components, request flow,
# advantages, limitations and a practical example.
# """

# response = ollama.generate(model="qwen3:0.6b", prompt=prompt3)

# print(response.response)