empty_directory = {} # create an empty dictionary object
print('------------')

initialized_directory = {2200001:"Changbeom Choi", 2200002:"Rohi Choi"}
print("Print the contents of 'initialized_directory'")
print(initialized_directory)
print('------------')

directory = {}
directory[2200003] = "Ji-Eun Kim"
print("Print the contents of 'directory'")
print(directory)
print('------------')

key = 2200003
if key in directory:
	print("The key " + str(key) + " is in the directory variable")
else:
    print("The key " + str(key) + " is not in the directory variable")

print('------------')
directory[2200002] = "Rohi Choi"
directory[2200001] = "Changbeom Choi"

print("Print the key and item of 'directory'")
for key, item in directory.items():
    print(key, ':', item)


print('------------')
print("Get item from 'directory' using key")
print(directory[2200003])