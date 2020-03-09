import random
import time
from functools import wraps
import bisect

def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.perf_counter()
        result = fn(*args, **kwargs)
        t2 = time.perf_counter()
        print("@timefn: {} took {} seconds".format(fn.__name__, t2 - t1))
        return result
    return measure_time

def linear_search(lst, number):
    for i in range(len(lst)):
        if lst[i] == number:
            return True
        else:
            pass
    return False

@timefn
def insertion01():
    important_data = []
    for i in range(10000):
        new_number = random.randint(0, 1000)
        important_data.append(new_number)
        important_data.sort()

@timefn
def insertion02():
    important_data = []
    for i in range(10000):
        new_number = random.randint(0, 1000)
        bisect.insort(important_data, new_number)

insertion01()
insertion02()