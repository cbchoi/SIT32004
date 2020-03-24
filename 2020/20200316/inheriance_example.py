import time
from PySide2.QtCore import QFile, Signal, Slot, QTimer, QObject

class Human(object):
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def get_name(self):
        return self.name

class Student(Human):
    def __init__(self, _name, _age, _id):
        super(Student, self).__init__(_name, _age)
        self.id = _id

    def get_id(self):
        return self.id

h = Human("Changbeom Choi", 39)
s = Student("Rohi Choi", 1, 2390001)

print(h.get_name())
print(s.get_name())

class Extend1(Human):
    def __init__(self, _name, _age):
        super(Extend1, self).__init__(_name, _age)

class Extend2(object):
    def __init__(self, _obj):
        self.obj = _obj

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def get_name(self):
        return self.name

class Extend3(object):
    def __init__(self, _name, _age):
        self.human = Human(_name, _age)

    def get_name(self):
        return self.human.name


ex1 = Extend1("Jieun Kim", 36)
print(ex1.get_name())

h = Human("Jieun Kim", 36)
ex2 = Extend2(h)
print(ex2.get_name())

ex3 = Extend3("Jieun Kim", 36)
print(ex3.get_name())

def print_a():
    print("a")

timer = QTimer()  # set up your QTimer
timer.timeout.connect(print_a)  # connect it to your update function
timer.start(5000)  # set it to timeout in 5000 ms

while True:
    print("1")
    time.sleep(1000)