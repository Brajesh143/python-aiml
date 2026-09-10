# Problem 1 — Two Sum
nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
    window = {}

    for index, value in enumerate(nums):
        rem = target - value

        if rem in window:
            return [window[rem], index]
        else:
            window[value] = index

    return []

print(twoSum(nums, target))