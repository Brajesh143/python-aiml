# 3. Reverse an array
# 4. Find second largest element
# 5. Remove duplicates
# 6. Move all zeros to the end
# 7. Find missing number

FirstNumbers = [10, 20, 30, 40, 50]
SecondNumbers = [10, 5, -20, 8, 15]
ThirdNumbers = [3, 1, 4, 5, 9, 2, 6, 5, 3, 5]
FourthNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
FifthNumbers = [1, 2, 3, 4, 5]

def reverse_array(arr):
    if not arr:
        return None

    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr

print(reverse_array(FourthNumbers))  # Output: [5, 4, 3, 2, 1]

def find_second_largest(arr):
    if not arr or len(arr) < 2:
        return None

    max = arr[0]
    second_max = arr[1]

    for num in arr:
        if (num > max):
            second_max = max
            max = num

        elif (num > second_max and num != max):
            second_max = num

    return second_max

    # first = second = arr[0]

    # for num in arr:
    #     if num > first:
    #         second = first
    #         first = num
    #     elif first > num > second:
    #         second = num

    # return second

print(find_second_largest(SecondNumbers))  # Output: 4
