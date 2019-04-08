class Human(object):
	def __init__(self, _name, _age):
		self.name = _name
		self.age = _age

	def ask_name(self):
		print("{}: Hi. What is your name?".format(self.name))

	def answer_name(self):
		print("{}: My name is {}.".format(self.name, self.name))

	def ask_age(self):	
		print("{}: How old are you?".format(self.name))
	
	def answer_age(self):
		print("{}: I am {}.".format(self.name, self.age))

gdhong = Human("Hong, Gil Dong", 20)
yhkim = Human("Kim, Younghee", 22)

# Initalize
h1_ask_name = gdhong.ask_name
h1_answer_name = gdhong.answer_name

h1_ask_age = gdhong.ask_age
h1_answer_age = gdhong.answer_age

h2_ask_name = yhkim.ask_name
h2_answer_name = yhkim.answer_name

h2_ask_age = yhkim.ask_age
h2_answer_age = yhkim.answer_age

# Protocol
h1_ask_name()
h2_answer_name()
h1_ask_age()
h2_answer_age()