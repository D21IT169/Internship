class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printval(self):
        print("Hey from Class A")

class B(A):    
    def printval(self):
        print("Hey from Class B")

class C(B):
    def printval(self):
        print("Hey from Class C")

objA = A("Hetvi", 10)
objB = B("Hetviii", 10)
objC = C("Hetviiiii", 10)


for i in (objA, objB, objC):
    print(i.name)
    print(i.age)
    i.printval()


