class car:
    @staticmethod
    def start():
        print("Car started")

class bmwCar(car):
    def __init__(self,name):
        self.name = name

c1 = bmwCar("Vijay")
c1.start()

