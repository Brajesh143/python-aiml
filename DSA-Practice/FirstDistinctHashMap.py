# Given a string, find the first character that appears only once.
s = "aabccddeff"

def findOnceOccurance(str):
  window = {}

  for i, value in enumerate(str):
    if value in window:
      window[value] += 1
    else:
      window[value] = 1

  for value in str:
    if window[value] == 1:
      return value

  return None

print(findOnceOccurance(s))