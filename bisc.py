class Calc:
    def __init__(self,marks,marks1):
        self.marks = marks
        self.marks1 = marks1
        #print(self.marks,self.marks1)

    def avg(self):
        c = self.marks + self.marks1
        return c

c1 = Calc(6,7)
b2 = Calc(10,20)
print(b2.avg())