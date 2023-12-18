grades_initial = {
    'Mathematics':None,
    'History':None,
    'English':None,
    'Religious Studies': None,
    'Chemistry': None,
    'Biology': None,
    'Geology':None

}

full_attendance = 190

def is_grade_valid(grade:int) -> bool:
    if grade < 0 or grade > 100:
        print(f"Something is wrong here! {grade} doesn't meet valid parameter!")
        return False
    return True
    
def valid_attendance(attendance:int) -> bool:
    if attendance < 0 or attendance > full_attendance:
        print('Attendance not within standard range!')
        return False
    return True

def subject_exists(subject:bool):
    if not subject in grades_initial:
        print(f'{subject} is not a valid subject!')
        return False
    return True

class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def printname(self):
        return(self.name, self.person_id)
    
    def change_name(self, new_name:str):
        if self.name == new_name:
            print(f'{new_name} is already {self.name}')
            return 
        
        self.name = new_name
        print(f'{self.name} set.')


class Student(Person):
    def __init__(self, name,  person_id, subject_grades=grades_initial, attendance=full_attendance):
        super().__init__(name, person_id)
        
        self.subject_grades = subject_grades

        self.attendance = attendance

    def update_grade(self, subject:str, grade:int):
        if is_grade_valid(grade):

            if subject not in self.subject_grades:
                print(f'{self.name} not assigned for this subject {subject}!')
                return 

            self.subject_grades[subject] = grade

        
    def add_subject(self, new_subject, grade = None):
        if grade and not is_grade_valid(grade):
            return
        

        if new_subject in self.subject_grades:
            print(f'{self.name} already assigned for {new_subject}!')
        else:
            self.subject_grades[new_subject] = grade
    
    def update_attendance(self, new_attendance:int):
        if not valid_attendance(new_attendance):
            return

        self.attendance = new_attendance
        print(f'Attendance updated: {self.attendance}!')


    def display_details(self):
        print(f'Name: {self.name}, ID: {self.person_id}, Attendance: {self.attendance}')
        print('Subjects-Grades: ')
        for subject,grade in self.subject_grades.items():
            print(f'{subject}: {grade}')


class Instructor(Person):
    def __init__(self, name, person_id, crs_taught = grades_initial):
        super().__init__(name, person_id)
        self.crs_taught = crs_taught

    def new_crs_taught(self, new_crs=bool):
        if new_crs and not subject_exists(new_crs):
            return
        
        if new_crs in self.crs_taught:
            print(f"{self.name} is already teaching the course!")
        else:
            self.new_crs = new_crs
            print(f"{self.name} has been added as an instructor {self.new_crs}!")

class Course(Instructor):
    def __init__(self, name, person_id, crs_taught, crs_code, crs_name, credit, students):
        super().__init__(name, person_id, crs_taught)
        self.crs_code = crs_code
        self.crs_name = crs_name
        self.credit = credit
        self.students = students