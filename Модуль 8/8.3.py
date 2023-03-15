from peewee import *


conn = SqliteDatabase('db1.sqlite')


class BaseModel(Model):
    class Meta:
        database = conn


class Students(BaseModel):

    id = PrimaryKeyField(unique=True)
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')


class Courses(BaseModel):

    id = PrimaryKeyField(unique=True)
    name = CharField(column_name='name')
    time_start = DateField(column_name='time-start')
    time_end = DateField(column_name='time-end')


class StudentCourses(BaseModel):

    student_id = ForeignKeyField(Students)
    course_id = ForeignKeyField(Courses)

    class Meta:
        db_table = 'Student_courses'


# Функция для создания словаря и добавления в таблицу через insert_many
def dictfill(keys, values):
    lst = []
    for v in values:
        d = {keys[i]: v[i] for i in range(len(keys))}
        lst.append(d)
    return lst


student_keys = ('name', 'surname', 'age', 'city')
courses_keys = ('name', 'time_start', 'time_end')
studentCourses_keys = ('student_id', 'course_id')

with conn:
    conn.create_tables([Students, Courses, StudentCourses])

    student_list = [
                ('Max', 'Brooks', 24, 'Spb'),
                ('John', 'Stones', 15, 'Spb'),
                ('Andy', 'Wings', 45, 'Manhester'),
                ('Kate', 'Brooks', 34, 'Spb'),
                ]
    Students.insert_many(dictfill(student_keys, student_list)).execute()

    courses_list = [
                ('python', '2021-07-21', '2021-08-21'),
                ('java', '2021-07-13', '2021-08-16')
                ]
    Courses.insert_many(dictfill(courses_keys, courses_list)).execute()

    student = Students.select()
    course = Courses.select()
    ids = [
        {'student_id': student[0].id, 'course_id': course[0].id},
        {'student_id': student[1].id, 'course_id': course[0].id},
        {'student_id': student[2].id, 'course_id': course[0].id},
        {'student_id': student[3].id, 'course_id': course[1].id},
        ]
    StudentCourses.insert_many(ids).execute()

    print('Студенты старше 30:')
    query1 = Students.select().where(Students.age >= 30)
    for item in query1:
        print(item.name, item.surname)
    print()

    print('Изучают Python:')
    query2 = Students.select().join(StudentCourses).join(Courses).where(Courses.name == 'python')
    for item in query2:
        print(item.name, item.surname)
    print()

    print('Изучают Python и из Spb:')
    query3 = Students.select().\
        where(Students.city == 'Spb').\
        join(StudentCourses).\
        join(Courses).\
        where(Courses.name == 'python')
    for item in query3:
        print(item.name, item.surname)
