# Numpy Basics

import numpy as np

# linespace

# It will return array with limits and 3rd parameter is number limit
# arr1 = np.linspace(1, 50, 20, dtype=int)
# print(arr1)

# # it will return identicle array
# arr2 = np.eye(2)
# print(arr2)


# # Random arrays: np.random.rand(), np.random.randn(), np.random.randint() 
# arr3 = np.random.rand(4, 50)
# print(arr3)

# # It will return a singlr random value between 4 and 50
# arr4 = np.random.randint(4, 50)
# print(arr4)

# arr5 = np.random.randn(4)
# print(arr5)

# arr6 = np.random.randint(10, 15, 2)
# print(arr6)
# print(type(arr6))

# arr7 = np.random.randint(11, 15, 6)
# print(arr7)

# arr8 = np.random.rand(5)
# print(arr8)
# print(type(arr8))

# arr9 = np.random.randn(5)
# print(arr9)

# shape, ndim, size, dtype 

# arr10 = np.array([[1, 2, 3], [4, 5, 6]]) 
# print(arr10)
# print(type(arr10))

# arr11 = np.shape(arr10) # Returns the dimensions of the array as a tuple. 
# print(type(arr11))
# print(arr11)
# print(arr10.ndim) # Returns the number of dimensions of the array.
# print(arr10.size) # It will return no of elements in array
# print(arr10.dtype) # It will return the type of element in array

# Indexing & Slicing
# 1D, 2D, and 3D array indexing

arr2D1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(arr2D1)
# print(type(arr2D1))

# arr2D2 = np.ones((3,3), dtype=int)
# print(arr2D2)

arr2D3 = np.array(arr2D1)
# print(arr2D3)
# print(arr2D3[arr2D3 > 3])
print(arr2D3[[0, 2]])

# print(type(arr2D3))

# Slicing arrays (arr[start:end])

# slice1 = arr2D3[2:3]
# print(arr2D3[::2, ::2])
# print(arr2D3[1::2])
# Step slicing (arr[::2])

# Boolean indexing

# Fancy indexing

# Array Operations
# Element-wise operations (+, -, *, /)

# Scalar operations

# Broadcasting rules

# Universal functions (np.add, np.multiply, np.sqrt, np.exp, np.log)
