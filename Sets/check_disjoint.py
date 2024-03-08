def areDisjoint(set1, set2, m, n):
    for i in range(0, m):
        for j in range(0, n):
            if (set1[i] == set2[j]):
                return False
    return True


set1 = [12, 34, 11, 5, 3]
set2 = [7, 2, 1, 5]
m = len(set1)
n = len(set2)

if areDisjoint(set1, set2, m, n):
    print("yes")
else:
    print("No")