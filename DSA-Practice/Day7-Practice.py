# DSA Practice — 20 min
# Don't look at previous solutions.

# Problem 1 — Two Sum
    # [2, 7, 11, 15]
    # target = 9
    # Return:
    # [0, 1]
    # Pair (HashMap) — O(n) solution.

# def twoSum(nums, target):
#     num_map = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_map:
#             return [num_map[complement], i]
#         num_map[num] = i
#     return []

# Explain O(n) solution.

# Problem 2 — Longest Substring
    # "abcabcbb"

    # Output:

    # 3

    # Use:

    # Sliding Window + Set/HashMap

s = "abcabcbb"
def longest_substring(s):

    last_seen = {}

    left = 0
    max_length = 0

    for i, char in enumerate(s):

        if char in last_seen:
            left = max(left, last_seen[char] + 1)

        last_seen[char] = i

        max_length = max(
            max_length,
            i - left + 1
        )

    return max_length

print(longest_substring(s))  # Output: 3


# Problem 3 — Valid Parentheses
    # "({[]})"

    # Output:

    # true

    # Use a Stack.



# Problem 4 — Linked List
    # 1 → 2 → 3 → 4 → 5

    # Find:

    # Middle → 3

    # Then reverse:

    # 5 → 4 → 3 → 2 → 1

    # Use:

    # slow / fast

    # and:

    # prev / current / next