import sqlite3
conn=sqlite3.connect("students.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    mark REAL,
    grade TEXT
)
""")
cursor.execute("DELETE FROM students")
students=[
    ("Alice",85),
    ("Hanna",90),
    ("Sara",80),
    ("Eva",95),
    ("Aira",99)
]

for name,mark in students:
    cursor.execute(
        "INSERT INTO students (name, mark) VALUES (?, ?)",
        (name, mark)
    )

conn.commit
cursor.execute("SELECT*FROM students")
rows=cursor.fetchall()
print("Student Records:")
for row in rows:
    print(row)
    conn.close()
