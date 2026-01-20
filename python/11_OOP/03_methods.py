class Student:
    college_name = "MUJ"
    name = "Vijay"
    def __init__(self, fullname,marks):
        print("Creating a new student in database")
        self.name = fullname
        self.marks = marks

    def welcome(self):
        print("Welcome", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Bhaskarraju",[99,100,98])
print(s1.name)          # Bhaskarraju
s1.welcome()            # Welcome Bhaskarraju
print(s1.get_marks())   # [99,100,98]