# Reverse an array using two pointer algorithm

arr = [1, 3, 4, 5, 7, 9]

def revArr(arr):
  if not arr:
    return None  # return empty array if input is empty

  left = 0
  right = len(arr) -1

  while(left <= right): # use python tuple swapping to swap the elements at left and right pointers
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

    left += 1
    right -= 1

  return arr

print(revArr(arr))
  