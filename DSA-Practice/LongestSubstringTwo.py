def unique_substring(s):
  window = {}
  left = 0
  length = 0
  maxLength = 0

  for right, value in enumerate(s):
    if value in window:
      left = window[value] + 1

    window[value] = right

    length = right - left + 1

    maxLength = max(maxLength, length)

  print("".join(window.keys()))

  return maxLength

s = "abcaefgh"

print(unique_substring(s))