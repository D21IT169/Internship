class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printval(self):     
        print("Hey from Class A")

class B:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printval(self):     
        print("Hey from Class B")

class C:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printval(self):       
        print("Hey from Class C")

objA = A("Hetvi", 10)
objB = B("Hetviii", 10)
objC = C("Hetviiiii", 10)

for i in (objA, objB, objC):
    i.printval()


