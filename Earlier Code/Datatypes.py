a = "hey"
b = 1
c = 1.1
d = 1j
e = ["apple", "banana"]
f = ("apple", "banana")
g = range(5)
h = {"Surname" : "Soni","Name" : "Hetvi"}
i = frozenset({"apple", "banana", "cherry"})
j = isinstance(5, int)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)


#byte
a = [10,20,30,40]  #list
b = bytes(a) #converting to the byte
print(b[0])
for i in b:
    print(i)
print("--")

#byte
a = [10,20,30,40]  #list
b = bytearray(a) #converting to the byte
b[1] = 200
for i in b:
    print(i)

#memoryview

    
