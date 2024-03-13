test_list = [("3", "ab"), ("1", "26"), ("7.32", "8"), ("Gfg", "8")]

print("The original list is : " + str(test_list))

res = []
for tup in test_list:
	temp = []
	for ele in tup:
		if ele.isalpha():
			temp.append(ele)
		else:
			temp.append(float(ele))
	res.append((temp[0],temp[1]))
print("The converted list : " + str(res))
