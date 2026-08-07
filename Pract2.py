# def analyze_marks(students):
#     # Find the topper.
#     topper = max(students, key=students.get)
    
#     # Find the lowest scorer.
#     lowest = min(students, key=students.get)
    
#     # Calculate the average marks.
#     total = sum(students.values())
#     average = total / len(students)
    
#     return {
#         "Topper": topper,
#         "Topper Marks": students[topper],

#         "Lowest Scorer": lowest,
#         "Lowest Marks": students[lowest],

#         "Average": average
#     }
    
#     # print(student_answer_dict)
# student_data = {
#     "Alice": 85,
#     "Bob": 72,
#     "Charlie": 91,
#     "David": 65,
#     "Eva": 78
# }

# result = analyze_marks(student_data)

# print(result)

text = "python is easy and python is powerful and easy"

remove_duplicate = set()

text_split = text.split(' ')
for i in text_split:
    remove_duplicate.add(i)
    
print(remove_duplicate)