class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal, newimg)


n1 = Complex(1,3)
n1.shownumber()

n2 = Complex(2,5)
n2.shownumber()

n3 = n1+n2
n3.shownumber()

