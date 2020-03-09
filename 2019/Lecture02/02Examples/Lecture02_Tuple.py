t1 = ([1], [1])
print(t1)
print(id(t1[0]), id(t1[1]))

t1[1][0] = 10
print(t1)
print(id(t1[0]), id(t1[1]))