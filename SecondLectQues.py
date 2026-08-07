# Strings

str = "Hello how are you?"
print(str)
print(type(str))
print(len(str)) # length of string
print(str[8]) # indexing
# str[5] = 'T'  string doesn't support item assignment
# print(str)



# Slicing (left to right 0 to n and right to left -1 to -n)
# In case of negative slice we can not go from max to min 
a = "This is my college"
print(a[1:4]) # his
print(a[:8]) # This is
print(a[5:]) #is my college
print(a[-5:-2]) # lle
print(a[:-4]) #This is my col
print(a[2:-2]) # is is my colle


# string functions
# str.endsWith(“er.“) #returns true if string ends with substr
# str.capitalize( ) #capitalizes 1st char
# str.replace( old, new ) #replaces all occurrences of old with new
# str.find( word ) #returns 1st index of 1st occurrence
# str.count(“am“) #counts the occurrence of substr in string
b = "this is my favourite book"

print(b.endswith("ok"))
print(b.endswith("bo"))
print(len(b))
print(b.capitalize())
print(b.replace("is", "er"))
print(b.find("o"))
print(b.count("o"))


# 1. WAP to input user'd first name and find print it's length

fname = input("Enter your first name \n")
length = len(fname)
print("Length of first name =",length)

# 2. WAP to find occurance of $ in a string

str = "Brajesh$Singh$#1298"
occurance = str.count("$")
print("Occurance of $ =",occurance)

# 3. WAP to check if a number entered by the user is odd or even.

number = int(input("Enter a number"))
if (number % 2 == 0):
    print("This is an even number")
else:
    print("This number is a odd number")

# 4. WAP to find the greatest nuber entered 3 numbers by user.

a = int(input("Enter first number \n"))
b = int(input("Enter second number \n"))
c = int(input("Enter third number \n"))

if (a > b and a > c):
    print("a is the greatest number")
elif(b > a and b > c):
    print("b is the greatest number")
else:
    print("c is the greatest number")

# 5. WAP to check if number is multiple of 7.

num = int(input("Enter a number \n"))
if(num % 7 == 0):
    print("num is multiple of 7")
else:
    print("num is not multiple of 7")
