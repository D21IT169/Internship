# X = sorted(list(T))
# T1 = []

# for i in range(K):
#     T1.append(X[i])

# for i in range((len(X)- K), len(X)):
#     T1.append(X[i])

# print(str[T1])




T = (4, 9, 1, 7, 3, 6, 5, 2)

print("enter the value of K")
K = int(input())


sorted1 = sorted(list(T))
T1 = []
for i in range(K):
    T1.append(sorted1[i])
    
for i in range((len(sorted1) - K), len(sorted1)):
    T1.append(sorted1[i])

# Printing 
print("Tuple : ", str(T))
print("K maximum and minimum values : ", str(T1))

