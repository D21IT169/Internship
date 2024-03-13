test_list = [(6, 24, 12), (7, 9, 6), (12, 18, 21)]

print("The original list is : " + str(test_list))

print("enter K")
K = int(input())

res = []
for i in test_list:
	c=0
	for j in i:
		if(j%K==0):
			c+=1
	if(c==len(i)):
		res.append(i)

# printing result
print("K Multiple elements tuples : " + str(res))
