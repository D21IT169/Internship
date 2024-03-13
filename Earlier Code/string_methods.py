txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)


txt = "Hello, And Welcome To My World!"
x = txt.casefold() 
print(x)

txt = "banana"
x = txt.center(20)
print(x)


txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.encode()
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

txt = "Hello, welcome to my world."
x = txt.find("welcome")
x = txt.index("welcome")
print(x)

txt1 = "My name is {fname}, I'm {age}".format(fname = "Hetvi", age = 20)
txt2 = "My name is {0}, I'm {1}".format("hetvi",21)
txt3 = "My name is {}, I'm {}".format("hetvi",22)

print(txt1)
print(txt2)
print(txt3)

txt = "Company12"
x = txt.isalnum()
print(x)

txt = "hetvi123"
x = txt.isascii()
print(x)

'''Join'''
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

txt = "Good night Sam!"
x = "mSa" #Replace this word
y = "eJo" #by this word
z = "odnght" # characters to be removed from the string
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))