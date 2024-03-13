def Sort_Tuple(tup):

	lst = len(tup)
	for i in range(0, lst):

		for j in range(0, lst-i-1):
			if (tup[j][-1] > tup[j + 1][-1]):
				temp = tup[j]
				tup[j] = tup[j + 1]
				tup[j + 1] = temp
	return tup


tup = [(30, 24, 30), (20, 10, 31), ('soni', 28, 32),
	('hetvi', 5), ('rency', 20), ('a', 15)]

print(Sort_Tuple(tup))
