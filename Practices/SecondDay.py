# Problem 1 — Two Sum — 12 min
# Input:
# [2, 7, 11, 15, 4, 5, 6, 9]

# Target:
# 9

# Output:
# [0, 1]

# def two_sum(nums, target):
#     seen = {}

#     for i, num in enumerate(nums):
#         complement = target - num

#         if complement in seen:
#             return [seen[complement], i]

#         seen[num] = i   

#     return []


# nums = [2, 7, 11, 15]
# target = 17

# result = two_sum(nums, target)

# print(result)

nums = [1, 2, 2, 3, 3, 3, 4]
freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
            
print(freq)         
            