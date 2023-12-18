import pandas as pd
import openpyxl
import management_system


df = pd.read_excel('person_database/DB.xlsx',sheet_name= ['student_db', 'instructor_db'])

student_df = df.get('student_db')
instructor_df = df.get('instructor_db')

num = 1


st_dt = student_df.at[num, 'Username']
st_id = student_df.at[num, 'ID']

tc_dt = instructor_df.at[num, 'Username']
tc_id = instructor_df.at[num, 'ID']
courses_taught  =  instructor_df.at[num, 'Courses']


# floras_grades = {'Mathematicss':65, 'History': 9}
# flora = Student(name="Florina", person_id=2, subject_grades=floras_grades)
# isaac_courses = {'Mathematics'}
# isaac = Instructor(name="Isaac Clarke", person_id=1, crs_taught=isaac_courses)
# print(flora.subject_grades)
# print(isaac.crs_taught)
# isaac.new_crs_taught('English')
# print(isaac.new_crs)
# isaac.new_crs_taught('Anime')
# flora.update_grade('Maths', 100)
# print(flora.subject_grades)
# flora.add_subject('English', 81)
# print(flora.subject_grades)
# flora.add_subject('Chems')
# print(flora.subject_grades)
# print(flora.name)
# print(flora.attendance)
# flora.update_attendance(300)
# print(flora.attendance)
st_dt.display_details()
