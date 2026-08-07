import ollama

response = ollama.generate(model="qwen3:latest",prompt="why is plant leaves green in color")
print(response)
# import re
# response_text= response.response
# actual_response= re.sub(r"<think>.*?</think>","",response_text,flags=re.DOTALL).strip()
# print(actual_response)