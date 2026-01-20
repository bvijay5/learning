class student:
    college_name = "MUJ"

    @staticmethod
    def hello():
        print("hello")
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks

    def printName(self):
        print(self.__name)

    def avg(self):
        sum = 0
        for no in self.__marks:
            sum = no+sum
        avg = sum/3
        print(f"Average marks of {self.__name} is: {avg}")


s1 = student("Vijay",[100,98,98])
s1.printName()
s1.avg()
s1.hello()