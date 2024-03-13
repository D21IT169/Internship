List1 = [(1,2), (3,4,5), (1,2,3,4,5,6), (1,2)]

print(List1)

print("enter the value of K")

k = int(input())

Filtered = [tup for tup in List1 if len(tup)!=k]

print(Filtered)