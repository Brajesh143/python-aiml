# Find the maximum sum of k consecutive elements.
# Not sorted

nums = [2, 1, 5, 1, 3, 2]
k = 3
range(3, 6)

def max_sum(nums, k):
    window_sum = sum(nums[:k])
    maximum = window_sum
    print(window_sum)

    for right in range(k, len(nums)): 
        window_sum += nums[right]
        window_sum -= nums[right - k]

        maximum = max(maximum, window_sum)

    return maximum

sum = max_sum(nums, k)
print(sum)
