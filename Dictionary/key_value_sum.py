dictionary = {1: 10, 2: 20, 3: 30}
sum = []


for key in dictionary:
	sum.append(key + dictionary[key])
	print(dictionary[key])

# Print the list
print("Key-value sum =", *sum)       #if * here then print in normal form and if no astrike then in list form 
