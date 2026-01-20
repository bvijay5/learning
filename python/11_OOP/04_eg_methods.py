class student:
    college_name = "MUJ"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for no in self.marks:
            sum = no+sum
        avg = sum/3
        print(f"Average marks of {self.name} is: {avg}")


s1 = student("Vijay",[100,98,98])
print(s1.name)
print(s1.marks)

s1.avg()
