# Dictionary

student = {
    "name": "Brajesh",
    "age": 29,
    "address": { # nested of dictionary
        "Flat": "304",
        "apartment": "Friends apartment",
        "sector": "sector 121, Gardhi Chaukandi",
        "city": "Noida",
        "state": "UP",
        "pin": "201307"
    }
}

# print(student)
# print(type(student))
# print(student["name"])
# print(student["address"])
# print(student["address"]["city"])

# functions of dictionary

print(student.keys())
print(type(student.keys()))
print(student.values())
print(student.items())
print(student.get("name")) # if key would not be available then it would return None