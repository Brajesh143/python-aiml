def max_element(arr):
  if not arr:
    return None
  max = arr[0]
  secondMax = arr[1]
  
  for i, value in enumerate(arr):
    if value > max:
      secondMax = max
      max = value
    elif value > secondMax and value < max:
      secondMax = value

  return secondMax

arr = [3, 9, 1, 18, 18, 15]
print(max_element(arr))
      