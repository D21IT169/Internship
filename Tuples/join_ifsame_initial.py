# test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13), (8, 0)]
# print("The original list is : " + str(test_list))

# res = []
# x = []

# for i in test_list:
# 	if i[0] not in x:
# 		x.append(i[0])    
# print(x)                              # store all the unique initial values
# print("DONE")

# for i in x:
# 	p = []
# 	p.append(i)
# 	print(p)                                        #store the first element (similar)
# 	for j in test_list:
# 		if i == j[0]:
# 			p.append(j[1])
# 	print(p)                                            #store the whole tuple uniquely
# 	print("-----") #5   6   7
# 	res.append(p)

# # printing result
# print("The extracted elements : " + str(res))

#Another method  (DOUBT)
myList = [(2, 5), (9, 4), (9, 0), (1, 4), (1, 5)]
print("Initially the list is : " + str(myList))

# joining tuples if similar initial element
joinList = []
for val in myList:										
	if joinList and joinList[-1][0] == val[0]:			
		joinList[-1].extend(val[1:])						
	else:
		joinList.append([ele for ele in val])	
joinList = list(map(tuple, joinList))

# Printing the joined List
print("Joined list : " + str(joinList))

