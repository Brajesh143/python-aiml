# List: A list stores multiple values in order.

# Features of List
# Ordered
# Changeable (mutable)
# Allows duplicates

a = [1, 9, 8, 4, 5, 5]
print(a)
print(type(a))

a.append(10)  # Add an element to the end of the list
print(a)

a.insert(2, 7)  # Insert an element at a specific index
print(a)

a.pop()  # Remove the last element from the list
print(a)

a.reverse()  # Reverse the order of the list
print(a)

a.sort()  # Sort the list in ascending order
print(a)

a.remove(5)  # Remove the first occurrence of a specific value
print(a)