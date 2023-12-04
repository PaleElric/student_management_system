import pandas as pd
import openpyxl
import management_system


df = pd.read_excel('person_database/DB.xlsx',sheet_name= ['student_db', 'instructor_db'])

student_df = df.get('student_db')
instructor_df = df.get('instructor_db')

num = 0


st_usrname = student_df.at[num, 'Username']
st_person_id = student_df.at[num, 'ID']
grade = student_df.at[num, 'Grade']
attendance = student_df.at[num, 'Attendance']
Student = [st_usrname, st_person_id, grade, attendance]

tc_usrname = instructor_df.at[num, 'Username']
tc_person_id = instructor_df.at[num, 'ID']
courses_taught  =  instructor_df.at[num, 'Courses']

