# Type conversion and Type casting

a = 10
b = 2
c = a / b
print(type(a))
print(type(b))
print(type(c))
print(c) # this type has been converted automatically that's why it is called type conversion

d = "10"
e = 2
f = int(d) / e # this is type casting
print(type(d)) # because d is string so we can not divide it, Now we need to convert this str into int for doing arithmatic operations
print(type(e))
print(type(f))
print(f)
