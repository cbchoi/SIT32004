
def print_obj(lst):
    print("---")
    for ob in lst:
        print(ob)

class Student(object):
    def __init__(self, string):
        self.name = string
#    def __str__(self):
#        return self.name

ob1 = Student("Nuke")
ob2 = Student("Mark")
ob3 = Student("Mat")

print_obj((ob1, ob2, ob3))
ob1 = ob2
print_obj((ob1, ob2, ob3))
ob3 = ob1
print_obj((ob1, ob2, ob3))

