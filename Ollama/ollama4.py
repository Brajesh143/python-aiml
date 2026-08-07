# GIVING MULTIMODEL INPUT TO MODEL
import base64
import ollama

# image_path= "img.png"

# with open(image_path,"rb") as f:
#     image_bytes= f.read()
# image_64= base64.b64encode(image_bytes).decode("utf-8")

# response= ollama.generate(model="llava:latest", images=[image_64], prompt="Describe the image  in a short paragraph")
# print(response.response)


# multiple images  as an input
image_paths = ["img.png","img_1.png", "img_2.png", "img_3.png"]

images_base64=[]
for i in image_paths:
    with open(i , "rb") as f:
        image_bytes= f.read()
        images_base64.append(base64.b64encode(image_bytes).decode("utf-8"))

response= ollama.generate(model="llava:latest", images=images_base64,
                          prompt="Generate an story based on these images, make sure you take context from each and every image in sequential order.")
print(response.response)