# Dictionary and Sets

'''
Store following word meanings in a python dictionary :
table : “a piece of furniture”, “list of facts & figures”
cat : “a small animal”
'''

# dict1 = {
#     "table": ["a piece of furniture", "list of facts & figures"],
#     "cat": "a small animal"
# }
# print(dict1)

'''
You are given a list of subjects for students. Assume one classroom is required for 1
subject. How many classrooms are needed by all students.
”python”, “java”, “C++”, “python”, “javascript”,
“java”, “python”, “java”, “C++”, “C”
'''

# set1 = set()
# print(type(set1))
# setOfSubject = {"python", "java", "python", "C++", "javascript", "java", "python", "java", "C++", "C"}
# print(type(setOfSubject))
# print(setOfSubject)
# print(len(setOfSubject))

'''
WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value.
'''

mydict = {}
print(type(mydict))

subject1Name = input("Enter subject1 name \n")
subject1Marks = input("Enter marks of subject1 \n")
newDictSubject1 = {
    subject1Name: subject1Marks
}
mydict.update(newDictSubject1)

subject2Name = input("Enter subject2 name \n")
subject2Marks = input("Enter marks of subject2 \n")
newDictSubject2 = {
    subject2Name: subject2Marks
}
mydict.update(newDictSubject2)

subject3Name = input("Enter subject3 name \n")
subject3Marks = input("Enter marks of subject3 \n")
newDictSubject3 = {
    subject3Name: subject3Marks
}
mydict.update(newDictSubject3)

print(mydict)

# Figure out a way to store 9 & 9.0 as separate values in the set.