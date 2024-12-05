class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.lap = self.Laptop()

    def show(self):
        print("student id is", self.id)
        print("student name is", self.name)
        self.lap.show()

    class Laptop:
        def __init__(self) -> object:
            self.ram = 4
            self.model = "HP"

        def show(self):
            print("laptop ram is", self.ram,self.model)


# l1 = laptop(9,"hp")
s1 = Student(9, "pavan")
s1.show()
