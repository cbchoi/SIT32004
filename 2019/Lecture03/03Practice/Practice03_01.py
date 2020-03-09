class student(object):
    def __init__(self):
        self.x = 10
        self.y = 20

    def translate(self, x, y):
        self.x += x
        self.y += y

    def __str__(self):
        return "cbchoi"
    
s = student()
print(s)
print(s.x, s.y)

s.translate(10, 20)
print(s.x, s.y)
