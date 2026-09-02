def is_valid(s):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:

        # Opening bracket
        if char in '([{':
            stack.append(char)

        # Closing bracket
        else:
            # Stack is empty
            if not stack:
                return False

            # Top doesn't match
            if stack[-1] != pairs[char]:
                return False

            # Remove matched opening bracket
            stack.pop()

    # Valid only if nothing is left
    return len(stack) == 0

print(is_valid("(([[{{{"))