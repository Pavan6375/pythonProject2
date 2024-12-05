import none


class School:
    def __init__(self, marks):
        self.marks = marks
        #self.marks2 = marks2
        print(marks)

    def show(self):
        for i in range(5):
            print("hello")

    def add(self,other,other1):
        c= other1 + other
        return c
    def mul(self,pa,ra):
        d = pa * ra
        return d
    def __sub__(self, othe,others):
        x = othe - others
        return x


a1 = School(4)
b1 = School(4)
a1.show()
print(a1.add(5,6))

print(b1.mul(6,7))
print(a1.__sub__(9,7))