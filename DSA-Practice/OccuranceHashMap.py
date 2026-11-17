# Find Occurance using hashmap

arr = [1, 2, 2, 3, 1, 1, 4]
def findOccurance(arr):
  freq = {}
  
  for i, value in enumerate(arr):
    if value in freq:
      freq[value] += 1
    else:
      freq[value] = 1

  return freq

print(findOccurance(arr))