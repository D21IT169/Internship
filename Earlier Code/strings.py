A = "hetvi"
print(A)

#String length
B = ""
print(B)
print(len(B))

#String as an array
print(A[2])
print(A[-2])

#Looping through strings 
for x in "Hello, python":
  print(x)

#Check strings (Sub)
H = "Welcome to Volansys!"
print("Welcome" in H)

if "Welcome" in H:
  print("Yes present")


#Check for not 
H = "Welcome to Volansys!"
print("too" not in H)

if "too" not in H:
  print("Not present")
  