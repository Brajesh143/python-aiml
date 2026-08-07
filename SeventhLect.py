# file input and output data

import os
# File open in read mode
# f = open("First.txt", "r")
# data = f.read()
# print(data)
# f.close()

# f = open("First.txt", "w")
# data = f.write("This is my new text") # Write will truncate the file
# f.close()

# f = open("First.txt", "a")
# data = f.write("\n This is my second text")
# f.close()

# f = open("Second.txt", "r")
# data = f.read() # this will show me the error because file doesn't exist
# print(data)
# f.close()

# f = open("Second.txt", "w")
# f.write("This is my next in my second file") # It will create a new file and write it on
# f.close()

# f = open("Third.txt", "a")
# f.write("This is my new text in third file") # It will also create a new file if file doesn't exist
# f.close()

# f = open("First.txt", "r+")
# data = f.read()
# f.write("I want to do operation for r+ mode") # This will write the data in file without truncate
# print(data)
# f.close()

with open("Second.txt", "a+") as f:
    f.write("\n I waana to the operation for a+ mode")

# os.remove("First.txt") # This will remove the file






