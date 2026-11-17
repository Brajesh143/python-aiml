# Concept: HashMap.
# Problem: Two Sum.

def twoSum(arr, target):
  window = {}
  for i, value in enumerate(arr):
    rem = target - value
    
    if rem in window:
      return [window[rem], i]
    else:
      window[value] = i
    print(window)
  return []

nums = [2, 7, 6, 11, 15]
target = 13
print(twoSum(nums, target))