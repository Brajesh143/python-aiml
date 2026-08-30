arr = [2, 1, 5, 1, 3, 2]
k = 3

max = 0
for i in range(0, len(arr)-2):
    if (arr[i] + arr[i+1] + arr[i+2] > max):
        max = arr[i] + arr[i+1] + arr[i+2]

print(max)