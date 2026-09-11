# 2. Longest Substring Without Repeating Characters ⭐⭐
# Given: s = "abcabcbb"

def uniqueSubstring(s):
  window = {}
  left = 0
  length = 0
  maxLength = 0

  for right, value in enumerate(s):
    if value in window:
      left = window[value] + 1

    window[value] = right

    length = right - left + 1

    print(left)

    maxLength = max(maxLength, length)

  print("".join(window.keys()))
  return maxLength

s = "abcabcbb"
print(uniqueSubstring(s))


# 3. Longest Substring with At Most K Distinct Characters ⭐⭐⭐

# Given: s = "eceba" k = 2

# "ece"
# Length = 3

def distinctK(s, k):
  freq_win = {}
  left = 0
  right = 0
  length = 0
  maxLength = 0

  for right, value in enumerate(s):

    if value in freq_win:
      freq_win[value] += 1
    else:
      freq_win[value] = 1

    while len(freq_win) > k:

      freq_win[value] = freq_win[value] - 1

      if freq_win[value] == 0:
        del freq_win[value]

      left = left + 1
  
    length = right - left + 1

    maxLength = max(maxLength, length)
    
  return maxLength
    
s = "eceba"
k = 2
print(distinctK(s, k))




# 4. Longest Repeating Character Replacement ⭐⭐⭐

# Given: s = "AABABBA" k = 1

# You can replace at most k characters.
# Find the longest substring that can be converted into a substring containing the same character.

# 5. Minimum Window Substring ⭐⭐⭐⭐

# Given: s = "ADOBECODEBANC" t = "ABC"

# Find the smallest substring of s that contains all characters of t.