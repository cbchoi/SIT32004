import random
import time

def linear_search(lst, number):
    for i in range(len(lst)):
        if lst[i] == number:
            return True
        else:
            pass
    return False

def binary_search(lst, number):
    if len(lst) == 0:
        return False
    else:
        mid_index = int(len(lst)/2)
        mid = lst[mid_index]

        if number < mid:
            return binary_search(lst[:mid_index], number)
        elif number > mid:
            return binary_search(lst[mid_index + 1:], number)
        elif number == mid:
            return True 
        else:
            return False

data = random.sample(range(-1000, 1000), 1000)
random.shuffle(data)
data.sort()

#print(data)
print(binary_search(data, 500))

