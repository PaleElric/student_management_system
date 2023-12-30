import pandas as pd
import openpyxl
from management_system import *


# df = pd.read_excel('person_database/DB.xlsx',sheet_name= ['student_db', 'instructor_db'])
#
# student_df = df.get('student_db')
# instructor_df = df.get('instructor_db')
#
# num = 0
#
#
# st_name = student_df.at[num, 'Username']
# st_id = student_df.at[num, 'ID']
# full_dt = st_name, st_id
#
# tc_dt = instructor_df.at[num, 'Username']
# tc_id = instructor_df.at[num, 'ID']
# courses_taught  =  instructor_df.at[num, 'Courses']

grades_1 = {
    'Mathematics':None,
    'History':86,
    'English':None,
    'Religious Studies': None,
    'Chemistry': None,
    'Biology': None,
    'Geology':None,

}

grades_2 = {
    'Mathematics':None,
    'History':72,
    'English':None,
    'Religious Studies': None,
    'Chemistry': None,
    'Biology': None,
    'Geology':None,

}


flora = Student(name="Florina", person_id=2, subject_grades=grades_1)
josh = Student(name="Josh", person_id=5, attendance=5, subject_grades=grades_2)
imo = Student(name="Imo", person_id=182, attendance=82)
stu = Student(name="Stu", person_id=47, attendance= 102)


peter = Instructor(name="Peter", person_id=10)
history = Course(crs_code=712, crs_name="History", credit=100)

print(peter.crs_taught)
peter.new_crs_taught(history)
peter.display_courses()
history.display_students()
history.add_student(flora)
history.add_student(josh)
history.add_student(imo)
history.add_student(stu)
print(history.calc_attendance())
print(history.calc_avg_grade())