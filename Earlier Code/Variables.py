#variable is created the moment you first assign a value to it
x = 5 
y = "Hetvi"
print(x)
print(y)

#Getting Type
print(type(x))
print(type(y))

#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3) 
print(x,y,z)


hetvi = "snakecase"
HETVI = "MACROCASE"
heTVI = "camelCase"
HeTvI = "CapWords"
print(hetvi, HETVI, heTVI, HeTvI)

#invalid varible names 
"""2myvar = "John"
my-var = "John"
my var = "John"
"""

#Assigning Multiple Values
A, B, C = "hello", "Good", "Morning"
print(A,B,C)

#One value to multiple variables 
C = D = E = "Same"
print(C,D,E)

#unpack collection
Numbers = 1, 2, 3
NewNo = Numbers
print(NewNo)
A = B = C = NewNo
print(A,B,C)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


#Output of Variables
M = "I'm fine"
print(M)

A = "Hey"
B = "Good"
C = "Morning"
print(A,B,C)
print(A + B + C)

A = 5
B = 5
print(A + B)

#Local variables (Scope within the function only)
def add():
    a = 10
    b = 5
    c = a + b
    print(c)
add() #call fun

#Global Variables 
H = 10

def demo():
    global H
    HH = 2
    print(H + HH)
demo()
print(H)
del H  #used to delete a variable
print(H)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic" #Here we change the value 
myfunc()
print("Python is " + x)


#Global variable in Inheritance
x = 10

def Demo():
   print (x)

Demo()


   