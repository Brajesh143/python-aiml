# Creating Arrays
import numpy as np

# Create a 1D NumPy array with values from 0 to 9.
# npArr1 = np.arange(0, 10)
# print(npArr1)

# # Create a 3×3 NumPy array filled with zeros.
# npArr2 = np.zeros((3, 3), int)
# print(npArr2)

# # Create a 4×4 identity matrix.
# npArr3 = np.eye(4, 4, k=0, dtype=int)
# print(npArr3)

# # Create an array of 10 random numbers between 0 and 1 using np.random.rand().
# npArr4 = np.random.rand(10)
# print(npArr4)

# # Create an array of even numbers from 2 to 20.
# npArr5 = np.arange(2, 21, 2)
# print(npArr5)

# Advanced questions

# Create a 5×5 matrix with 1 on the border and 0 inside.

# npArr6 = np.zeros((5, 5), dtype=int)
# print(npArr6)
# npArr6[0, :] = 1
# npArr6[1:5, 0] = 1
# npArr6[1:5, 4] = 1
# npArr6[1:,0:1] = 1
# npArr6[1:4, 4] = 1
# npArr6[4, 0:4] = 1
# npArr6[4, 4] = 1
# print(npArr6)

# matrix = np.pad(np.zeros((3, 3), dtype=int), pad_width=1, mode='constant', constant_values=2)
# print(matrix)

# npArr7 = np.ones((5, 5), dtype=int)
# npArr7[1:-1, 1:-1] = 0
# print(npArr7)

# Create a 5×5 checkerboard pattern (alternating 0 and 1).
# npArr8 = np.ones((5,5), dtype=int)
# rows, cols = npArr8.shape
# print(npArr8[0: -1])

# print(rows)
# print(npArr8)

# Create a diagonal matrix where diagonal elements are [10, 20, 30, 40].

# Create an array where values increase from 1 to 25 in a snake-like pattern.

# Create a 4×4 array with random integers from 0–9, but replace the diagonal with np.nan.

#  Practice Questions (with topics)
# Create two arrays [1, 2, 3, 4] and [5, 6, 7, 8]. Perform addition, subtraction, multiplication, and division element-wise.

# a = np.array([5, 10, 15])
# b = np.array([1, 2, 3])

# add = a + b
# print(add)

# sub = a - b
# print("substract", sub)

# mul = a * b
# print("multiply", mul)

# div = a / b
# print("division", div)

# Scalar Operations
# Take an array [2, 4, 6, 8]. Multiply each element by 3 and subtract 5.

# c = np.array([2, 4, 6, 8])
# print(c * 3)
# print(c - 5)


# Broadcasting
# Add a column vector [[1], [2], [3]] with a row vector [10, 20, 30] using broadcasting.
# Try adding two arrays of shape (3,2) and (3,3). What happens?
arr1 = np.arange(1, 7).reshape(2, 3)
# arr1 = np.arange(1, 4)
arr2 = np.arange(1, 10).reshape(3, 3)

# print(arr1)
# print(arr2)
arr3 = arr1 + arr2
print(arr3)

# a = np.array([[1, 2, 3],
#               [4, 5, 6]])

# b = np.array([10, 20, 30])  # shape (3,)

# print(a + b)

# Universal Functions
# Create an array [1, 4, 9, 16] and apply:
# Square root
# Exponential
# Natural logarithm
# Given arr = np.array([0, np.pi/2, np.pi]), compute:
# sin(arr)
# cos(arr)
# tan(arr)