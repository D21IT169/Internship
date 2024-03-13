test_tuple = ([5, 6], [6, 7, 8, 9], [3])

print("The original tuple : " + str(test_tuple))


res=[]
for i in test_tuple:
	res.extend(i)
res=tuple(res)

print("The flattened tuple : " + str(res))
