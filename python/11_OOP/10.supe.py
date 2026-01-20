class car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("Car started")

class bmwCar(car):
    def __init__(self,name, type):
        super().__init__(type)
        self.name = name
        super().start()

c1 = bmwCar("Vijay","Electric")
print(c1.type)

