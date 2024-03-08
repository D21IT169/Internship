print("-------------INIT METHOD---------------")
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
A1 = A("hetvi", 10)
print(A1.name)
print(A1.age)


print("-------------STR METHOD---------------")

class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def __str__(self):
       return f"{self.name}({self.age})"

A1 = A("hetvi", 10)
print(A1)    


print("-------------Object METHOD---------------")

class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def func(self):
        print("Hello from ", self.name)

A1 = A("Hetvi", 30)
A1.func()


print("------Can use any name on place of self---------------")

class A:
    def __init__(hetvi, name, age):
        hetvi.name = name
        hetvi.age = age 

    def __str__(self):
       return f"{self.name}({self.age})"

A1 = A("hetvi", 10)
print(A1)    


print("-----------We can modify the value later ---------------")

class Person:
  count = 0     # define variable 
  def __init__(self, name, age):
    self.name = name
    self.age = age
    Person.count+=1  #acccess variable by the add value

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
print(Person.count)         #print the count
p1.name = "Hetvi"
p1.myfunc()
print(p1.name)

print("----------We can also delete the values in obj---------------")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1.age
del p1                           #can also delete the object 
print(p1.age)





