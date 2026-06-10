import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

#create data
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks REAL
)
""")
conn.commit()

#insert data
def insert_students(name, marks):
    cursor.execute(
        "INSERT INTO students(name, marks) VALUES(?, ?)",
        (name, marks)
    )
    conn.commit()
    print("Student added successfully")


#view_all_students
def get_all_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if rows:
        print("\n all students :")
        for row in rows:
            print(row)
    else:
        print("no student found")

#search by id
def get_students_by_id(student_id):
    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("Student found:")
        print(student)
    else:
        print("Student not found")

#uodate marks
def update_marks(students_id,new_marks):
    cursor.execute("UPDATE students SET marks =? WHERE id=?",(new_marks,students_id))
    conn.commit()

if cursor.rowcount>0:
    print("marks updated successfully")
else:
    print("student not found")

#delete students
def delete_students(student_id):
    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully")
    else:
        print("Student not found")

#students above threshold
def get_students_above(threshold):
    cursor.execute(
        "SELECT * FROM students WHERE marks > ?",
        (threshold,)
    )

    rows = cursor.fetchall()

    if rows:
        print(f"\nStudents above {threshold}:")
        for row in rows:
            print(row)
    else:
        print("No matching students found")

#main program
def main():
    create_table()
while True:

    print("\n=====STUDENTS DATABASE SYSTEM====")
    print("1.add students")
    print("2.view all students")
    print("3.search students by id")
    print("4.update students")
    print("5.delete students")
    print("6.students above marks")
    print("7.exit")

    choice = input("enter your choice :")
    if choice == "1":
        name = input("enter name :")
        marks = float(input("enter marks"))
        insert_students(name,marks) 

    elif choice == "2":
        get_all_students()

    elif choice == "3":
        students_id = int(input("enter student id :"))
        get_students_by_id(students_id)

    elif choice == "4":
        students_id = int(input("enter student id :"))  
        new_marks = float(input("enter new marks :"))
        update_marks(students_id,new_marks)

    elif choice == "5":
        students_id = int(input("enter student id :"))
        delete_students(students_id)
        
    elif choice == "6":
        threshold = float(input("enter threshold marks :"))
        get_students_above(threshold)

    elif choice == "7":
        print("exiting program ") 
        conn.close()   
        break
    else:
        print("invalid  choice.please try again")