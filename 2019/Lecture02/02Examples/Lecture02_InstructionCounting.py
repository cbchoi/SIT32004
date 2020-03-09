import time

idx = 0

def factorial(num):
    global idx
    idx += 1
    if num == 1:
        idx += 1
        return 1
    else:
        idx += 1
        return factorial(num -1) * num

value = 10
start = time.clock()
print("10!= " + str(factorial(value)))
end = time.clock()
print("Elapsed Time:" + str(end - start) + " seconds")

print(idx)