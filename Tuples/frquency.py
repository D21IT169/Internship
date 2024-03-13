test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)

X = {}
for elem in test_tup:
	if elem in X:
		X[elem] += 1
	else:
		X[elem] = 1

print("Tuple elements frequency is : " + str(X))
