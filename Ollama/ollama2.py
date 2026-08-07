import ollama

# chunk = ollama.generate(
#     model="qwen3:8b",
#     prompt="Tell me a story about a man in 200 words?",
    # stream=True,
    # options={"temperature": 0.7}
# )

# print(chunk.response)

# for i in chunk:
#     print(i.response, end="")

#FOR MODELS WITH THINKING CAPABILITIES
response = ollama.generate(model="qwen3:8b",prompt="why is plant leaves green in color")
import re
response_text= response.response
actual_response= re.sub(r"<think>.*?</think>","",response_text,flags=re.DOTALL).strip()
print(actual_response)