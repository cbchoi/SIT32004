'''
class Human(object):
	attr1 = 10
	def __init__(self):
		self.property1 = 0
		self.property2 = 1

	def print_property(self):
		print(self.property1)
		print(self.property2)
	

h = Human()
h.attr1 = 22

b = Human()
print(b.attr1)
print(h)

print(h.print_property)
h.print_property()

a = Human()
Human.attr1 = 20  # attr1 is a class variable

b = Human()
print(b.attr1)
'''

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
