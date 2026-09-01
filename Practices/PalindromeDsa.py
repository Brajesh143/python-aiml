# Check whether a string is a palindrome.

str = "ABCDBA"

def checkPalindrome(word):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False

        else:
            left += 1
            right -=1

    return True


check = checkPalindrome(str)
if check:
    print("Yes, String is palindrome")
else:
    print("No, String is not palidrome")