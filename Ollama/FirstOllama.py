import ollama

#generate model

# response = ollama.generate(
#     model="llama3:8b",
#     prompt="What is the meaning of life?",
# )

# print(response.response)

# Thinking capability

# import re

# response = ollama.generate(
#     model="qwen3:8b",
#     prompt="What is the meaning of life?",
# )

# response_text = response.response

# response_text = re.sub(r"<script.*?>.*?</script>", "", response_text, flags=re.DOTALL)

# print(response_text)

# Stream

# stream = ollama.generate(
#     model="llama3:8b",
#     prompt="What is the meaning of life?",
#     stream=True,
# )

# for chunk in stream:
#     print(chunk.response, end="")

# vision capability

import base64

image_path = "img_1.png"

with open(image_path, "rb") as image_file:
    image_data = image_file.read()
    image_base64 = base64.b64encode(image_data).decode("utf-8")

response = ollama.generate(
    model= "llava:latest",
    images=[image_base64],
    prompt="What is in the image?",
)

print(response.response)