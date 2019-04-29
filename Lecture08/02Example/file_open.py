"""file_open.py"""
import random

f = open("test.txt", "w")

for i in range(100):
	f.write(str(random.randint(0, 100)))
	f.write("\n")

f.close()