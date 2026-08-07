# Variable-Length Arguments

# Useful when you don't know how many arguments will be passed.
# *args: Collects positional arguments into a tuple.

# def sum(*args):
#     total = 0
#     for i in args:
#         total += i
        
#     print(total)
    
# sum(10, 12)
# sum(10, 20, 30, 40)

# **kwargs: Collects keyword arguments into a dictionary.
# def create_dict(**student):
#     print(type(student))
#     print(student['name'])
    
# create_dict(name="Brajesh", age=29)

# def add(a, b):
#     print(a + b)
    
# result = add(10, 20)
# print(result)

# def add(a, b):
#     return a+b
    
# result = add(10, 20)
# print(result)