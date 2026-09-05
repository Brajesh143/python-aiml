# Find minimum element

numbers1 = [10, 20, 30, 40, 50]
numbers2 = [10, 5, -20, 8, 15]
numbers3 = [3, 1, 4, 5, 9, 2, 6, 5, 3, 5]

def find_minimum(arr):
    if not arr:
        return None

    min = arr[0]

    for num in arr:
        if num < min:
            min = num

    return min

print(find_minimum(numbers3))  # Output: 1

print(min(numbers2))  # Output: 1