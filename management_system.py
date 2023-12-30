grades_initial = {
    'Mathematics': None,
    'History': None,
    'English': None,
    'Religious Studies': None,
    'Chemistry': None,
    'Biology': None,
    'Geology': None,

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


def subject_exists(subject: bool):
    if not subject in grades_initial:
        print(f'{subject} is not a valid subject!')
        return False
    return True


class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def user_details(self):
        return self.name, self.person_id

    def change_name(self, new_name:str):
        if self.name == new_name:
            print(f'{new_name} is already {self.name}')
            return

        self.name = new_name
        print(f'{self.name} set.')

    def __str__(self):
        return f"Person: {self.person_id} - {self.name}"

    def erase(self:str):
        if self.name is None:
            print(f"{self.name} does not exist on the system!")
        else:
            print(f"{self.name} has been removed from the system!")
            del self.name, self.person_id
            return


class Student(Person):
    def __init__(self, name,  person_id, subject_grades=grades_initial, attendance=full_attendance):
        super().__init__(name, person_id)

        self.subject_grades = subject_grades
        self.attendance = attendance

    def __str__(self):
        return f"{self.person_id}, {self.name}, {self.subject_grades}, {self.attendance}"

    def update_grade(self, subject: str, grade: int):
        if is_grade_valid(grade):

            if subject not in self.subject_grades:
                print(f'{self.name} not assigned for this subject {subject}!')
                return

            self.subject_grades[subject] = grade

    def add_subject(self, new_subject, grade=None):
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
        try:
            if self.name is None:
                print(f"{self.name} doesn't exist!")
            else:
                print(f'Name: {self.name}, ID: {self.person_id}, Attendance: {self.attendance}')
                print('Subjects-Grades: ')
                for subject,grade in self.subject_grades.items():
                    print(f'{subject}: {grade}')
        except AttributeError:
            print("There are no attributes for the user!")


class Course:
    def __init__(self, crs_code, crs_name, credit):
        self.crs_code = crs_code
        self.crs_name = crs_name
        self.credit = credit
        self.student_list = list()

    def add_student(self, new_student: Student):
        if type(new_student) is not Student:
            raise Exception("Expected Student Class!")
        if new_student in self.student_list:
            print("Student already on the course!")
        else:
            self.student_list.append(new_student)
            print(f"New Student Added: {new_student}")

    def calc_attendance(self):
        total_students = len(self.student_list)
        attendance_sum = 0

        if total_students == 0:
            print("Can't calculate for 0 students")
            return

        for student in self.student_list:
            attendance_sum += student.attendance

        avg_sum = attendance_sum / total_students

        return avg_sum

    def calc_avg_grade(self):
        total_students = 0
        grade_sum = 0

        if len(self.student_list) == 0:
            print("No students!")
            return

        for student in self.student_list:
            student_grade = student.subject_grades.get(self.crs_name)
            if student_grade is None:
                pass
            else:
                grade_sum += student_grade
                total_students += 1

        return grade_sum / total_students

    def display_students(self):
        for student in self.student_list:
            print(student)

    def __str__(self):
        return f"Course: {self.crs_name}, {self.crs_code}, {self.credit}"


class Instructor(Person):
    def __init__(self, name, person_id):
        super().__init__(name, person_id)
        self.crs_taught = list()

    def __str__(self):
        return f"Instructor: {self.name}, {self.person_id}, {self.crs_taught}"

    def new_crs_taught(self, new_crs:Course):
        if new_crs in self.crs_taught:
            print(f"{self.name} is already teaching the course!")
        else:
            self.crs_taught.append(new_crs)
            print(f"{self.name} has been added as an instructor {new_crs.crs_name}!")

    def display_courses(self):
        print(f"Instructor: {self.name}, is assigned to courses: ")
        for course in self.crs_taught:
            print(course)