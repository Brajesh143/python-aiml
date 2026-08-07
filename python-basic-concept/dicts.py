# Dictionary

# user = [
#     {
#         "name": "Brajesh",
#         "age": 30,
#         "city": "New York",
#         "is_student": False,
#         "hobbies": ["reading", "traveling", "cooking"]
#     },
#     {
#         "name": "John",
#         "age": 25,
#         "city": "Los Angeles",
#         "is_student": True,
#         "hobbies": ["gaming", "watching movies"]
#     },
#     {
#         "name": "Jane",
#         "age": 28,
#         "city": "Chicago",
#         "is_student": False,
#         "hobbies": ["dancing", "painting"]
#     },
#     {
#         "name": "Bob",
#         "age": 35,
#         "city": "Houston",
#         "is_student": False,
#         "hobbies": ["swimming", "cycling"]
#     }
# ]


# for i, person in enumerate(user):
#     print(f"Person {i + 1}:")
#     for key, value in person.items():
#         print(f"  {key}: {value}")

# nums = [10, 45, 2, 99, 23]

# sorted_nums = sorted(nums)
# print(sorted_nums)

# print(sorted_nums[len(sorted_nums) - 1])

# print(max(nums))
# print(min(nums))

# fruits = ["apple", "banana", "mango"]

# for index, fruit in enumerate(fruits):
#     print(f" {index + 1} fruit name is {fruit}")

# nums = [1, 2, 3, 4, 5]
# sum = 0
# for num in nums:
#     sum += num
# print(sum)

# 1. Create a list of 5 numbers and print it

# list5 = [10, 20, 30, 40, 50]
# print(list5)

# for i in range(1, 6):
#     print(i)

# 2. Print first element of list
# list1 = [10, 20, 30, 40, 50]
# print(list1[0])

# 3. Print last element of list

# print(list1[len(list1) - 1])

# 4. Add new item to list using append()

# list1.append(60)
# print(list1)

# 1. Create a list of 5 numbers and print all numbers using loop

list1 = [10, 23, 30, 45, 50]

# for num in list1:
#     print(num)


# 2. Find the largest number in a list

# print(max(list1))

# Example:

# [10, 45, 2, 99, 23]
# 3. Count even numbers in a list

# even_count = 0

# for num in list1:
#     if num % 2 == 0:
#         even_count += 1

# print(even_count)

# filtered_list = list(filter(lambda x: x % 2 == 0, list1))
# print(len(filtered_list))

# 4. Reverse a list without using built-in reverse function

# list2 = [4, 5, 3, 1, 9, 10, 6]

# print(list(reversed(list2)))

# reversed_list = []
# for i in range(len(list2) - 1, -1, -1):
#     reversed_list.append(list2[i])
# print(reversed_list)


# 5. Remove duplicate values from a list

Input = [1, 2, 2, 3, 4, 4]

# unique_values = list(set(Input))
# print(unique_values)

# unique = []

# for i in Input:
#     if i not in unique:
#         unique.append(i)
# print(unique)


# 6. Create a dictionary for a student

# Store:

# name
# age
# marks

# Then print all values.

dict1 = {
    "name": "Brajesh",
    "age": 30,
    "marks": 80
}

# print(dict1)

for key, value in dict1.items():
    print(f"{key} : {value}")

# 7. Add a new key "city" to dictionary

dict1["city"] = "New York"
print(f"Dictionary with city: {dict1}")

# 8. Update marks in student dictionary

# Example:

# 80 → 95

dict1["marks"] = 95
print("Updated dictionary:", dict1)

# 9. Loop through dictionary and print:
# name : Rahul
# marks : 90
# 10. Check if key "email" exists in dictionary


if "email" in dict1:
    print("Email key exists in dictionary")
else:    
    print("Email key does not exist in dictionary")


# 11. Create a list of student dictionaries

# Example:

# [
#  {"name": "A", "marks": 80},
#  {"name": "B", "marks": 90}
# ]

dict2 = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 90},
    {"name": "C", "marks": 85},
    {"name": "D", "marks": 95},
    {"name": "E", "marks": 88}
]

for student in dict2:
    print(student["name"])


# 12. Print names of all students from list of dictionaries
# 13. Find student with highest marks

print(max(dict2, key=lambda x: x["marks"]))

# 14. Search student by name

# Input:

# Enter student name

# Output:

# Student found
# 15. Count frequency of words using dictionary

# Input:

# "apple banana apple mango banana"

