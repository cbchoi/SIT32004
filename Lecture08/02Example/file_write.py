"""file_open.py"""
import random

f = open("test.txt", "w")

for i in range(100):
	f.write(str(random.randint(0, 100)))
	f.write("\n")

f.close()

f1 = open("append.txt", "a")
f2 = open("test.txt", "r")

for line in f2:
	f1.write(str(int(line) + 10))
	f1.write("\n")

f1.close()
f2.close()