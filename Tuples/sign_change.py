test_list = [(3, -1), (-4, -3), (1, 3), (-2, 5), (-4, 2), (-9, -3)]

print("The original list is : " + str(test_list))

res = []
for sub in test_list:
	res.append((abs(sub[0]), -abs(sub[1])))
print("Updated Tuple list : " + str(res))
