import sqlite3


def fprint(tup):
    for item in tup:
        print(item[0])
    print()


conn = sqlite3.connect('db1.sqlite')
cursor = conn.cursor()

cursor.execute("CREATE TABLE Students (id int, name Varchar(32), surname Varchar(32), age int, city Varchar(32))")
cursor.execute("CREATE TABLE Courses (id int, name Varchar(32),  time_start date, time_end date)")
cursor.execute("CREATE TABLE Student_courses (student_id int, course_id int)")

cursor.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?)", [(1, 'Max', 'Brooks', 24, 'Spb'),
                                                                   (2, 'John', 'Stones', 15, 'Spb'),
                                                                   (3, 'Andy', 'Wings', 45, 'Manhester'),
                                                                   (4, 'Kate', 'Brooks', 34, 'Spb')])
cursor.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)", [(1, 'python', '2021-07-21', '2021-08-21'),
                                                               (2, 'java', '2021-07-13', '2021-08-21')])

cursor.executemany("INSERT INTO Student_courses VALUES (?, ?)", [(1, 1), (2, 1), (3, 1), (4, 2)])

conn.commit()

cursor.execute("SELECT name FROM Students WHERE age >= 30")
print('Студенты старше 30:')
fprint(cursor.fetchall())

tmp = cursor.execute("SELECT id FROM Courses WHERE name == 'python'")
tmp = tmp.fetchall()[0][0]
cursor.execute("SELECT name FROM Students JOIN Student_courses "
               f"ON Students.id = Student_courses.student_id WHERE course_id == {tmp}")
print('Проходят курс по Python:')
fprint(cursor.fetchall())

cursor.execute("SELECT name FROM Students JOIN Student_courses "
               "ON Students.id = Student_courses.student_id WHERE course_id == 1 AND city == 'Spb'")
print('Проходят курс по Python из Спб:')
fprint(cursor.fetchall())

conn.close()
