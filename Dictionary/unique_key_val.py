def UniqueKeys(arr):


    res = list(set(val for dic in arr for val in dic.keys()))

    print(str(res))


arr = [{'my': 1, 'name': 2}, 
    {'is': 1, 'my': 3},
    {'ria': 2}]

UniqueKeys(arr)



#Unique Value
test_list = [{'gfg': 1, 'is': 2}, {'best': 1, 'for': 3}, {'CS': 2}]


print("The original list : " + str(test_list))


res = list(set(val for dic in test_list for val in dic.values()))

print("The unique values in list are : " + str(res))