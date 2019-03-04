# calculate 10!
import time
from functools import wraps

def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.perf_counter()
        result = fn(*args, **kwargs)
        t2 = time.perf_counter()
        print("@timefn: {} took {} seconds".format(fn.__name__, t2 - t1))
        return result
    return measure_time

def factorial(num):
    if num == 1:
        return 1
    else:
        print("Caluating " + str(num) + "!")
        return factorial(num -1) * num

@timefn
def profiling_factorial():
    value = 10
    result = factorial(value)
    print("10!= " + str(result))

if __name__ == "__main__":
    profiling_factorial()