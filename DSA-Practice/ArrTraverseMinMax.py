# Problem 2: Find the largest and smallest elements in an array in a single traversal.
def findMaxMin(arr):
  if not arr:
    return None

  max = arr[0]
  min = arr[0]
  
  for ar in arr:
    if ar > max:
      max = ar
    elif ar < min:
      min = ar

  return max, min

arr = [13, 12, 12, 10, 18]
print(findMaxMin(arr))