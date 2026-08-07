numbers = [10, 20, 10, 30, 20, 40]
# insert data
# we can use three function to insert data into a list
# 1. append
# 2. insert
# 3. extend
# numbers.append([90, 99, 101])
# print(numbers)

# numbers.insert(2, 50)
# print(numbers)

# numbers.extend([11, 15, 22])
# print(numbers)

# Update data into list
# There are two way to update the value in list
# 1. Update using index
# 2. Update multiple value using slicing

# numbers[2] = 22
# print(numbers)

# numbers[4] = 55
# print(numbers)

# numbers[6] = 100
# print(numbers) // Error

numbers[1:3] = [15, 17]
print(numbers)


# sequence[start : stop : step]
# start → Index where slicing begins (default = 0)
# stop → Index where slicing ends (exclusive)
# step → Number of positions to move each time (default = 1)
numbers = [1, 4, 2, 7, 9]
# print(numbers[:1:1])
# print(numbers[::1])

# Delete data from list
# numbers.pop()
# print(numbers)

# numbers.remove(4) // removed  value
# print(numbers)
# numbers.pop(3) // removed 3rd index
# print(numbers)

# del numbers[3]
# print(numbers)

# numbers.clear()
# print(numbers)

# Reverse 
# There are three method use for reverse a list reverse, slice and reversed

# numbers.reverse()
# print(numbers)

# print(numbers[::-1])

# reversed_number = list(reversed(numbers))
# print(reversed_number)


