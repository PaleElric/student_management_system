import pandas as pd
import openpyxl


dataframe = pd.read_excel('person_database/database.xlsx',sheet_name= ['student_database', 'instructor_database'])

student_df = dataframe.get('student_database')
instructor_df = dataframe.get('instructor_databse')

print(student_df[1])

# class Person:
#     def __init__(self, name, person_id):
#         self.name = name
#         self.person_id = person_id

    
#     def printname(self):
#         print(self.name, self.person_id)

# class Student(Person):
#     def __init__(self, name, person_id, grades, attendance):
#         super().__init__(name, person_id)
#         self.grades = grades
#         self.attendance = attendance

# x = Student(student_df[1])
# print(x.grades, x.attendance)

# class Instructor(Person):
#     def __init__(self, name, person_id, courses_taught):
#         super().__init__(name, person_id)
#         self.courses_taught = courses_taught

# class Course(Student, Instructor):
#     def __init__(self, name, person_id, grades, attendance):
#         super().__init__(name, person_id, grades, attendance)
    