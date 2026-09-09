def longest_substring(s):

    window = {}
    left = 0
    length = 0
    maxLength = 0

    for right, value in enumerate(s):
      if value in window:
        left = window[value] + 1

      window[value] = right
      print("----", window)

      length = right - left + 1

      maxLength = max(maxLength, length)

    print(window)
    print(left)
    return maxLength

s = "abbdcxbyb"
print(longest_substring(s))