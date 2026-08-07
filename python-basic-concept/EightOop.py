# class Student:
#     name="Brajesh"

# s1 = Student()
# print(s1.name)

# class Student:
#     name = "Brajesh"
#     def __init__(self):
#         print("This is a constructor")
# s1 = Student()
# print(s1.name)

class Student:
    def __init__(self, name):
        self.myname = name

    def hello(self):
        print(self.myname)

    @staticmethod
    def myName():
        print("Brajesh is my name")

s1 = Student("Brajesh")
print(s1.myname)
print(s1.hello())
print(s1.myName())
