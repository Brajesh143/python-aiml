import base64
import ollama

image_paths = ["img.png", "img_1.png", "img_2.png", "img_3.png"]

images_base64 = []

for image_path in image_paths:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        image_base64 = base64.b64encode(image_data).decode("utf-8")
        images_base64.append(image_base64)

response = ollama.generate(
    model="llava:latest",
    images=images_base64,
    prompt="Create a story based on the images.",
)

print(response.response)