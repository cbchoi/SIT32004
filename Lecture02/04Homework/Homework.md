# Homework02
Solve the following problems 
1. Analyze the following code and explain why second code is allowed
* First Code
```python
t1 = (1, 2)
t1[1] = 10
print(t1)
```

* Second Code
```python
t1 = ([1], [1])
print(t1)
 
t1[1][0] = 10
print(t1)
```

2. Analyze the following code and explain why function insertion02 is faster
```python
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
```