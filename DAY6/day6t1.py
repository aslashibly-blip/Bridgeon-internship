import json
students=[
    {"name":"Arun","age":20,"grade":"A"},
    {"name":"Akhil","age":21,"grade":"B"},
    {"name":"Ajay","age":19,"grade":"C"},
    {"name":"Zara","age":22,"grade":"B"},
    {"name":"Liya","age":20,"grade":"A"}
]
with open("students.json","w") as f:
    json.dump(students,f,indent=2)
with open("students.json","r") as f:
    print(f.read())
