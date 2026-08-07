#SYSTEM INSTRUCTION
import ollama

response = ollama.generate(model="llama3:8b",prompt="why is the ocean blue", system="You are an funny assistant , you explain things in funny way")
print(response.response)


# OPTIONS PARAMETER
# response = ollama.generate(model="llama3:8b",prompt="why is the ocean blue",
#                            options={
#                                "temperature":0.3,
#                                "top_p":0.5,
#                                "top_k":45
#                            })


print(response.response)
