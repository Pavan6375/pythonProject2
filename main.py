class computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram= ram
        print("ram is", self.cpu,self.ram)

    def config(self):
        print("config ", self.cpu, self.ram)

comp1 =computer("i8",8)
comp2 =computer("i9",10)
comp3 = computer("i7",3)
comp1.config()
comp3.__init__("i5",8)




