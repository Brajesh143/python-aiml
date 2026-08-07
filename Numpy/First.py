import numpy as np

# arr = np.arange(0, 10)
# print(arr)

# arr1 = np.arange(1, 50, 2)
# print(arr1)

# list1 = [1, 2, 3, 4, 5]
# print(np.array(list1))

# arr = np.zeros(3)
# print(arr)

# arr = np.ones(4)
# print(arr)

# arr1 = np.linspace(1, 50, 10)
# print(arr1)

# arr2 = np.eye(4)
# print(arr2)

# arr = np.random.rand(10)
# print(arr)

# arr = np.random.randn(4, 4)
# print(arr)

# arr = np.random.randint(1, 100)
# print(arr)

# arr = np.random.randint(1, 100, 10)
# print(arr)

# arr = np.arange(25)
# print(arr)

# print(arr.max())
# print(arr.min())
# print(arr.argmax())
# print(arr.argmin())

# arr2d = arr.reshape(5, 5)
# print(arr2d)

# print(arr)
# print(arr.shape())
# print(arr1d)

# Zeros
# arrZeros = np.zeros(3, int, 'F') # it will return 1D zeros
# print(arrZeros)

# arrZeros2D = np.zeros((3,4), int)
# print(arrZeros2D)

# ones
# arrOne = np.ones(4, int) # It will return a 1D array with integer
# print(arrOne)

# arrOne2D = np.ones((3,4), int)
# print(arrOne2D)

# linespace

# arrLineSpace = np.linspace(1, 50, 10)
# print(arrLineSpace)

#eye

# arrEye = np.eye(4)
# print(arrEye)

# random

# arr = np.random.rand(4,4)
# print(arr)

# arrN = np.random.randn(4,4)
# print(arrN)

# arrInt = np.random.randint(5, 10, 4)
# print(arrInt)

#shape and reshape
# arr = np.arange(1, 10)
# print(arr)
# reshapesArr = arr.reshape(3,3)
# print(reshapesArr)
# print(arr)
# shapeArr = np.shape(reshapesArr)
# print(shapeArr)

# Numpy Indexing
# arr = np.arange(1, 11)
# print(arr)

# print(arr[2:])

# print(arr[:4])

# print(arr[4:6])

# print(arr[4:])

# arr[0:2] = 100
# print(arr)

#2D array

arr = np.arange(1,10)
twodArr = arr.reshape(3,3)
# print(twodArr)

print(twodArr[0:2,1:3])