# Function and Recursion
# def sum(a, b):
#     print(a + b)
# sum(4,3)


# def table(n):
#     for i in range(1, 11):
#         print(n * i)
# table(5)

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n - 1)
factNumber = fact(5)
print(factNumber)


