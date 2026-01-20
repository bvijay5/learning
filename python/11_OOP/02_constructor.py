class Student:
    college_name = "MUJ"
    name = "Vijay"
    def __init__(self, fullname,marks):
        print(self)
        print("Creating a new student in database")
        self.name = fullname
        self.marks = marks


s1 = Student("Bhaskarraju",[99,100,98])
print(s1.name)          # Bhaskarraju
print(s1.marks)         # [99, 100, 98]
print(Student.name)     # Vijay
print(s1.college_name)  # MUJ

