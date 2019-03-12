
class human(object):
    def __init__(self):
        self.name = "---"
        self.age = -1

    def introduce(self):
        pass

class student(human):
    def __init__(self):
        human.__init__(self)
        self.id = 2100001

    def introduce(self):
        print("My name is {}. My id is {}".format(self.name, self.id))
        self.study()

    def study(self):
        print("I study a lot")

class professor(human):
    def __init__(self):
        self.id = 10000

# if this object is student object then call introduce method, study method
# else if this object is professor object then call introduce method, teach method

s = student()
print(type(s))

s.introduce()
