import json

# student_dict = {
#     "name": "Brajesh",
#     "age": 25,
#     "marks": 85
# }

# converted_json = json.dumps(student_dict)
# print("Converted JSON String:", converted_json)
# print("Type of converted_json:", type(converted_json))

# print("Original Student Dictionary:", student_dict)
# print("Type of student_dict:", type(student_dict))

# student_dict_new = {
#     'name': 'Brajesh',
#     'age': 25,
#     'marks': 85
# }

# print("Original Student Dictionary:", student_dict_new)
# print("Type of student_dict_new:", type(student_dict_new))

# student_json = '{"name": "Brajesh", "age": 30}'

# converted_str = json.loads(student_json)
# print("Converted Python Dictionary:", converted_str)
# print("Type of converted_str:", type(converted_str))
# print("Original Student JSON:", student_json)
# print("Type of student_json:", type(student_json))

students_dict = [
    {
        "name": "A",
        "age": 20,
        "marks": {
            "Math": 90,
            "Science": 85,
            "English": 88
        }
    },
    {
        "name": "B",
        "age": 22,
        "marks": {
            "Math": 90,
            "Science": 85,
            "English": 88
        }
    },
    {
        "name": "C",
        "age": 21,
        "marks": {
            "Math": 85,
            "Science": 80,
            "English": 82
        }
    }
]

with open("new_students.json", "w") as file:
    json.dump(students_dict, file)

# students_dict_json = json.dumps(students_dict)
# print("Students Dictionary in JSON Format:")
# print(students_dict_json)

# with open("students.json", "w") as file:
#     json.dump(students_dict_json, file)

# with open("students.json", "r") as file:
#     students_data = json.load(file)
# print("Students Data from JSON File:")
# print(students_data)
# print("Type of students_data:", type(students_data))