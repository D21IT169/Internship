tuple1 = (1, 4)
tuple2 = (3, 9)
print("First tuple : " + str(tuple1))
print("Second tuple : " + str(tuple2))

# finding all pair Combination of tuples 
pairCombi = [] 
for val1 in tuple1:
    for val2 in tuple2:
        tup = [val1, val2]
        pairCombi.append(tuple(tup))

for val1 in tuple2:
    for val2 in tuple1:
        tup = [val1, val2]
        pairCombi.append(tuple(tup))

# Printing tuple Combination 
print("All pair Combinations are  : " + str(pairCombi))
