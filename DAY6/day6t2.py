import json
with open ("students.json","r") as f:
    students = json.load(f)
for student in students:
    print(f"name:{student['name']},grade:{student['grade']},age:{student['age']}")