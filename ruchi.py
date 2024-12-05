


class A:
    def feature1(self):
        print("print feature 1")

    def feature2(self):
        print("print feature 2")

a1=A()
a1.feature1()

class C(A):
    def feature5(self):
        print("jai balaya")

c1= C()
c1.feature1()
c1.feature2()
from ruchi import A


class B(A):
    def feature3(self):
        print("print feature 3")

    def feature4(self):
        print("print feature 4")

b1 =B()
b1.feature1()

