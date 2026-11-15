# Find the sum of all elements in an array.
def sum(arr):
  if not arr:
    return None

  sum = 0
  
  for ar in arr:
    sum += ar

  return sum

arr = [3, 12, 12, 10, 18]
print(sum(arr))