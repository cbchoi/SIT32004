"""file_readlines_writelines.py"""
import random

f = open("test.txt", "r")

lst = f.readlines()
f.close()
print(lst)

f = open("dup_test.txt", "a")
f.writelines(lst)
f.close()

f1 = open('test.txt', "r")
f2 = open("dup_test.txt", "r")

lst_f1 = f1.readlines()
lst_f2 = f2.readlines()

if len(lst_f1) != len(lst_f2):
	print("Two files are not same")
else:
	for i in range(len(lst_f1)):
		if lst_f1[0] != lst_f2[0]:
			print("Two files are not same")
	else:
		print("Two files are same")