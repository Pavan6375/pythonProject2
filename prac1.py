from threading import *
from time import sleep

import thread


class Pavan(Thread):
    def run(self):
        for i in range(5):
            print("pavan is a good boy")
            sleep(1)


class Ruchita(Thread):
    def run(self):
        for i in range(5):
            print("ruchita is a bad girl")
            sleep(1)


a = Pavan()
b = Ruchita()
a.start()
sleep(0.05)
b.start()
a.join()
b.join()
print("bye")
