# calculate 10!
import time

def factorial(num):
	if num == 1:
		return 1
	else:
		return factorial(num -1) * num


value = 10
start = time.clock()
print("10!= " + str(factorial(value)))
end = time.clock()
print("Elapsed Time:" + str(end - start) + " seconds")