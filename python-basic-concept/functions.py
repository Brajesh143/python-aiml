def sayHello():
    print("Hello, World!")

sayHello()
sayHello()


def yourName(name):
    print(f"My name is {name}.")

yourName("Alice")
yourName("Bob")

def add(a, b):
    return a + b

add(10, 20)

result = add(10, 20)

print(result)

# Lambda function (anonymous function)
add = lambda a, b: a + b
print(add(3, 20))

subtract = lambda a, b: a - b
print(subtract(10, 5))

nums = [1, 2, 3, 4]

map_result = list(map(lambda x: x*x, nums))

print(map_result)

squares = list(map(lambda x: x*x, nums))

print(squares)

filtered_result = list(filter(lambda x: x % 2 == 0, nums))
print(filtered_result)

is_even = lambda x: x % 2 == 0
print(is_even(4))  # True
print(is_even(7))  # False

a = [1, 2, 3]
b = [4, 5, 6]

result = map(lambda x, y: x - y, a, b)

print(list(result))

students = [
    {"name": "A", "marks": 70},
    {"name": "B", "marks": 90},
    {"name": "C", "marks": 80}
]

sorted_students = sorted(
    students,
    key=lambda x: x["marks"]
)

print(sorted_students)

data = ["Alice", "", "Bob", "", "Charlie"]

print(data)

valid = list(filter(lambda x: x != "", data))

print(valid)

texts = ["Hello", "World", "Python", "Programming"]
cleaned = list(map(lambda x: x.upper(), texts))
print(cleaned)

mul = lambda a, b: a * b
print(mul(8, 4))

cube = lambda x: x ** 3
print(cube(4))

input = [1, 2, 3, 4, 5, 6]

doubled = list(map(lambda x: x ** 2, input))

print(doubled)

odd_number = list(filter(lambda x: x % 2 != 0, input))
print(odd_number)

input = [2, 4, 3, 1, 9, 5]

sorted_input = sorted(map(lambda x: x, input))

print(sorted_input)

input = [(1, 50, 10), (2, 20, 5), (3, 40, 15)]

sorted_input = sorted(input, key=lambda x: x[2])

print(sorted_input)

input = [1, 2, 3, 4]

squared = list(map(lambda x: x ** 2, input))

print(squared)

input = ["apple", "banana", "cherry"]

map_result = list(map(lambda x: x.upper(), input))
print(map_result)

a = [1, 2, 3]
b = [4, 5, 6]

result = map(lambda x, y: x + y, a, b)
print(list(result))

input = ["1", "2", "3"]

result = list(map(lambda x: int(x), input))

print(result)

input = ["apple", "banana", "cherry"]

map_result = list(map(lambda x: len(x), input))
print(map_result)

