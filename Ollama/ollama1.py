import ollama

# response = ollama.generate(
#             model="llama3:8b",
#             prompt="Tell me a story about a cat in 200 words?",
#             options={"temperature": 0.7, "max_tokens": 200},)
# print(response.response)


prompt = input("How may I help you? \n")

respose = ollama.generate(
    model="llama3:8b",
    prompt=prompt,
)

print(respose.response)

