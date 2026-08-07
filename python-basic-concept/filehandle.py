# File handling in Python

# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("data.txt", "w") as file:
#     file.write("This is a new line of text.\n")
#     file.write("This is another line of text.\n")

# with open("data.txt", "a") as file:
#     file.write("This line is appended to the file.\n")

# with open("data.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# with open("data.txt", "r") as file:
#     lines = file.readlines()

# print(lines)

# with open("data.txt", "r") as file:
#     for line in file:
#         print(line.strip())
#         print(type(line))

# with open("data.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)
#     print(type(lines))

# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)
#     print(type(content))

# with open("data1.txt", "x") as file:
#     file.write("This file is created using 'x' mode.\n")
#     file.write("It will raise an error if the file already exists.\n")

# with open("data1.txt", "w") as file:
#     file.write("This file is created using 'w' mode.\n")
#     file.write("It will overwrite the file if it already exists.\n")

import os

# if os.path.exists("data1.txt"):
#     with open("data1.txt", "r") as file:
#         content = file.read()
#         print(content)
# else:
#     print("The file does not exist.")


# os.remove("data1.txt")