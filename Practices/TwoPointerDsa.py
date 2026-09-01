nums = [1, 2, 3, 4, 6]
target = 6

# Find two numbers whose sum is 6.
# This is sorted array

def findNumbers(input, target):
    left = 0
    right = len(input) -1

    while left < right:
        total =  input[left] + input[right]

        if total == target:
            return [left, right]

        elif total > target:
            right -= 1

        else:
            left += 1

    return []

numbers = findNumbers(nums, target)

print(numbers)