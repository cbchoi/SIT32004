empty_lst = []
print('------------')

initialized_lst = ["Changbeom Choi", "Rohi Choi"]
print("Print the contents of 'initialized_lst'")
print(initialized_lst)
print('------------')

lst = initialized_lst
lst.append("Ji-Eun Kim")
print("Print the contents of 'lst'")
print(lst)

print('------------')
print("Get item from 'lst' using index")
print(lst[1])

print('------------')
print("Print conents of 'lst'")
for item in lst: # iteration 
	print(item)

print('------------')
print("Remove item from 'lst' using index")
lst.remove('Rohi Choi')
for item in lst:
	print(item)

print('------------')
print("Removing last item from 'lst'")
removed_item = lst.pop()
print("Removed item:", removed_item)
print("Rest of the contents")
for item in lst:
	print(item)
