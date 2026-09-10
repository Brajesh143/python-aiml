# Frequency of Characters

def fequency(s):
  freq = {}

  for value in s:
    if value in freq:
      freq[value] = freq[value] + 1
    else:
      freq[value] = 1

  return freq

s = "aabbccabcd"
print(fequency(s))