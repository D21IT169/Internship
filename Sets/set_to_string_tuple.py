set_val = {"python","is","difficult","to","learn"}
print(set_val)
print(type(set_val))


str_val = " ".join(set_val)
print(str_val)
print(type(str_val))

print("-----------------------------Set to tuple-----------------------------------------")

s = {'a', 'b', 'c', 'd', 'e'}
print(type(s), " ", s)


t = tuple(s)

# print tuple
print(type(t), " ", t)

print("--------------------------------tuple to set-----------------")
#program to convert tuple into set
t = ('x', 'y', 'z')

print(type(t), " ", t)


s = set(t)
print(type(s), " ", s)

