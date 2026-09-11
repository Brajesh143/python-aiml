class Employee:
    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    def get_details(self):
        return f"ID: {self.id}, Name: {self.name}, Department: {self.department}, Salary: {self.salary}"

    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

employee1 = Employee(1, "John Doe", "Engineering", 60000)
print(employee1.get_details())

print("Increasing salary by 10%...")
print(employee1.increase_salary(10))
print(employee1.get_details())


class Developer(Employee):
    def write_code(self):
        return f"{self.name} is writing code."

class SeniorDeveloper(Developer):
    def review_code(self):
        return f"{self.name} is reviewing code."

print("\nCreating a Senior Developer...")
developer1 = Developer(3, "Kate", "Engineering", 50000)
senior_dev = SeniorDeveloper(2, "Jane Smith", "Engineering", 80000)
print(senior_dev.get_details())
print(developer1.get_details())
print(developer1.write_code())
print(senior_dev.review_code())

employees = {
    1: {"name": "John", "department": "Engineering"},
    2: {"name": "Mike", "department": "HR"},
    3: {"name": "Kate", "department": "Finance"}
}

# class EmployeeNotFoundError(Exception):
#     pass

def get_employee_details(employee_id):
    if employee_id in employees:
        return employees[employee_id]
    else:
        # raise EmployeeNotFoundError(f"Employee with ID {employee_id} not found.")
        raise ValueError(f"Employee with ID {employee_id} not found.")


print(get_employee_details(5))  # Should return details for John