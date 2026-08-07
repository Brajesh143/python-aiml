# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# movieList = []
# name1 = input("Enter your first fav movie name \n")
# movieList.append(name1)

# name2 = input("Enter your 2nd fav movie name \n")
# movieList.append(name2)

# name3 = input("Enter your 3rd fav movie name \n")
# movieList.append(name3)

# print(movieList)

'''WAP to count the number of students with the “A” grade in the following tuple.
    [”C”, “D”, “A”, “A”, “B”, “B”, “A”]
'''

# tuple1 = ("C", "D", "A", "A", "B", "B", "A")
# print(type(tuple1))
# print(tuple1)

# countA = tuple1.count("A")
# print(countA)


# Store the above values in a list & sort them from “A” to “D”

# list1 = ["C", "D", "A", "A", "B", "B", "A"]
# tuple1tolist = list(tuple1)
# print(tuple1tolist)
# print(type(tuple1tolist))
# tuple1tolist.sort()
# print(tuple1tolist)


'''WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
    [1, 2, 3, 2, 1] and [1, abc, abc, 1]
'''

list1 = [1, 2, 3, 2, 1]
copyList = list1.copy()
list1.reverse()
print(list1)
if (copyList == list1):
    print("This list contains palindrome number")
else:
    print("This list doesn't contains palindrome number")

