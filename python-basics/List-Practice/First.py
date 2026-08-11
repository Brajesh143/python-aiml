# List Practice

# A list is a built-in Python data structure used to store multiple items in a single variable. Lists are ordered, mutable (changeable), and can contain elements of different data types.

# Functions to add element in List
# append()
# insert()
# extend()

# Function to remove element in list
# remove()
# pop()
# clear()
# del

# Question:
# 1. Create a list of 5 fruits and:

# fruits = ["Apple", "Mango",  "Banana", "Papaya", "Guava"]

# # Print the entire list.
# print("Fruits list", fruits)

# # Print the first element.
# print(f"First element is {fruits[0]}.")

# # Print the last element.
# print(f"Last element of the fruits is {fruits[-1]}.")

# 2. Given the list:

# numbers = [10, 20, 30, 40]
# Add 50 at the end.
# length = len(numbers)
# numbers.insert(length, 50)
# numbers.append(50)

# numbers.extend([2, 3, 4])
# number2 = [1, 5, 7]

# new_list = numbers + number2

# numbers += number2

# print(new_list)



# # Insert 15 at index 1.
# # numbers[1] = 15
# numbers.insert(1, 15)

# # Remove 30.
# numbers.remove(30)

# # Print the updated list.
# print(numbers)

# marks = [78, 95, 67, 88, 92]

# # Total number of elements
# print(f"Length: {len(marks)}")

# # Maximum value
# print(f"Maximum value: {max(marks)}")

# # Minimum value
# print(f"Minimum value: {min(marks)}")

# # Sum of all elements
# print(f"Sum: {sum(marks)}")

# colors = ["Red", "Green", "Blue", "Yellow"]

# # Print each color on a new line using a loop.
# for color in colors:
#     print(color, "\n")

# numbers = [12, 5, 8, 17, 20, 33, 42]

# even = odd = 0
# for number in numbers:
#     if number % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# # Number of even numbers
# print(f"Even number {even}")

# # Number of odd numbers
# print(f"Odd number {odd}")