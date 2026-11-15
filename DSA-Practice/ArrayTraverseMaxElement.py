def max_element(arr):
  if not arr:
    return None
  max = arr[0]
  
  for i, value in enumerate(arr):
    if value > max:
      max = value

  return max

arr = [3, 2, 12, -5, 10, 5]
print(max_element(arr))
      