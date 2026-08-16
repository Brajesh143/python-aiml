# class Employee:
#     def greet(self):
#         print("Hello")

# employee1 = Employee()

# employee1.greet()

class Employee:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)


employee1 = Employee("Alice")
employee2 = Employee("Bob")

employee1.greet()
employee2.greet()