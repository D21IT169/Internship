def find_common(list1, list2, list3):
    common = set()
    for elem in list1:
        if elem in list2 and elem in list3:
            common.add(elem)
    return common

list1 = [10]
list2 = [20]
list3 = [30]

common = find_common(list1, list2, list3)
print(common)