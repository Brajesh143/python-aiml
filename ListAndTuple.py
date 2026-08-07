# List and Tuple
emptyList = []
print(type(emptyList))
emptyList.insert(0, 2)
print(emptyList)
list0 = ["Brajesh"]
print(type(list0))
list1 = ["Brajesh", 29, 76, "Noida"]
print(type(list1))
print(list1)

# changes in lists
list1[0] = "Student"
print(list1) # ['Student', 29, 76, 'Noida'] that means lists are mutable

# Functions in list
list2 = [4, 9, 1, 3, 5, 2, 9]
# list2.append(7)
# print(list2)

# list2.sort()
# print(list2)

# list2.sort(reverse=True)
# print(list2)

# list2.reverse()
# print(list2)

# list2.insert(2, 6)
# print(list2)

# list2.remove(9) # it will remove the value of first occurance
# print(list2)

# list2.pop(2) # it will remove data from a particular index
# print(list2)

# # Tuple
tuple0 = ("Brajesh Singh", ) # if you want to create a tuple and you have only element you should add a comma their
print(type(tuple0))
tuple1 = ("Brajesh", 29, 76, "Noida", 1, 2, 76, 2, 2, 1)
print(type(tuple1))
print(tuple1)

# # changes in tuple
# tuple1[0] = "Student"
# print(tuple1) # It reurns error that means tuple is immutable

print(tuple1.index(76))
print(tuple1.count(2))

