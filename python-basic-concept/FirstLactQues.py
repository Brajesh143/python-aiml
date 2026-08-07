# Write a programe to input two numbers and print their sum.

a = input("Enter a value")
print(a)

a = int(input("Enter one interger value \n"))
b = int(input("Enter 2nd interger value \n"))

c = a + b

print("Sum of a and b =",c)


# # WAP to input side of a square and print it's area
side = int(input("Enter side of square \n"))

area = side**2

print("Area of square =", area)

# WAP to input two floating point numbers and print their average

float1 = float(input("Enter 1st float number \n"))
float2 = float((input("Enter 2nd float number \n")))

avg = (float1 + float2) / 2

print("Average of", float1 ,"and", float2 ,"is", avg)

# WAP to input two integer number a and b
# Print True if a is greater than or equal to b else false

a = int(input("Enter value of a \n"))
b = int(input("Enter value of b \n"))

if a >= b:
    print(True)
else:
    print(False)