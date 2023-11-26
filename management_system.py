import pandas as pd


dataframe = pd.read_excel('person_database/database.xlsx',sheet_name= ['student_database', 'instructor_database'])

student_df = dataframe.get('student_database')
instructor_df = dataframe.get('instructor_databse')

num = 1

usr_name = student_df.at[num, 'Username']
person_id = student_df.at[num, 'ID']
grade = student_df.at[num, 'Grade']
attendance = student_df.at[num, 'Attendance']

class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    
    def printname(self):
        print(self.name, self.person_id)

class Student(Person):
    def __init__(self, name, person_id):
        super().__init__(name, person_id)
        self.grades = grade
        self.attendance = attendance

x = Person(usr_name, person_id)
xy = Student(usr_name, person_id)
print(x.name, x.person_id, xy.grades, xy.attendance)

# class Instructor(Person):
#     def __init__(self, name, person_id):
#         super().__init__(name, person_id)
#         self.courses_taught = courses_taught

# class Course(Student, Instructor):
#     def __init__(self, name, person_id, grades, attendance):
#         super().__init__(name, person_id, grades, attendance)
    