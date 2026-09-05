numbers = [10, 20, 30, 40, 50]

numbers1 = [10, 5, -20, 8, 15]

numbers2 = []

# 1. Find maximum element

# print(max(numbers))
# print(numbers[-1])

# HashMap Implementation

def find_maximum_element(arr):
    if not arr:
        return None

    max_element = arr[0]

    for num in arr:
        if num > max_element:
            max_element = num

    return max_element

print(find_maximum_element(numbers2))
