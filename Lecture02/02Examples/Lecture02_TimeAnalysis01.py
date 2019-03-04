import random

def linear_search(lst, number):
    for i in range(len(lst)):
        if lst[i] == number:
            return True 
        else:
            pass

data = list(range(10000))
random.shuffle(data)

print(linear_search(data, 500))