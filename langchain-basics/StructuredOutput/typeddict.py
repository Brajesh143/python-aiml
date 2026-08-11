from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = { 'name': "Brajesh", 'age': 30 } 
# new_person: Person = { 'name': "Brajesh", 'age': '30' } // It will accept whether the data is in correct data type. If I will pass age as string it will also work.

print(new_person)