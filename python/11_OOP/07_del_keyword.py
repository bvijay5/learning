class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

# del {obj.attribute/object}
# deletes the attiribute or object itself

s1 = Student("vijay",123)
print(s1.name)
del s1.name
print(s1.roll_no)

