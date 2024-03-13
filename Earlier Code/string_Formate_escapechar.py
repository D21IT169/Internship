A = 21
B = "My age is {}"
print(B.format(A))


A = "hetvi"
B = 21
C = "nadiad"
D = "My name is {}, age {}, living in {}"
E = "My name is {2}, age {1}, living in {0}"   #variable order indexing
print(D.format(A,B,C))
print(E.format(A,B,C))

#Escaped Characters "Double Quotes"
print("Hetvi \"Soni\"")
print("Hetvi \\Soni\\")
print("Hetvi \nSoni")
print("Hetvi \rHetvi")
print("Hetvi \tSoni")
print("Hetvi \fSoni")

txt = """\rWhy, hello there 
wonderful stackoverflow\r people!"""
print(txt)

txt = "Hello\rWorld!"
print(txt) 

print("Hello\rWorld")