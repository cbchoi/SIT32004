# calculate 10!
import time

def factorial(num):
    if num == 1:
        return 1
    else:
        print("Caluating " + str(num) + "!")
        return factorial(num -1) * num

def profiling_factorial():
    value = 10
    start = time.perf_counter()
    result = factorial(value)
    print("10!= " + str(result))
    end = time.perf_counter()
    print("Elapsed Time:" + str(end - start) + " seconds")

if __name__ == "__main__":
    profiling_factorial()