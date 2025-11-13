class School:
    school_name = "ABC Public School"  # class variable

    def __init__(self, student_name, grade, roll_no):
        self.student_name = student_name
        self.grade = grade
        self.roll_no = roll_no

student1 = School("Alice", 10, 23)
print(student1.student_name, student1.grade, student1.roll_no, student1.school_name)
