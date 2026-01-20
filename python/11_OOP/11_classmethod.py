class Person:
    name = "Anonymos"

    def changeName(self, name):
        self.__class__.name = "Vijay"

    @classmethod
    def changename(cls, name):
        cls.name = name

        