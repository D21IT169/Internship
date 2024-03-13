rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

print("----------------------------")

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=' ')
    print('')

print("----------------------------")

rows = 5
for i in range(0,rows):
    for j in range(0,rows-i-1):
        print(end=' ')
    for j in range(0, i+1):
        print(j, end=" ")
    print()

print("------------------------")

rows = 5
for i in range(rows,0,-1):
    for j in range(0,rows-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()


print("------------------------")

rows = 6
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
    print('')

print("------------------------")

rows=5
for i in range(rows):
    print(" "*(rows-i-1)+'* '*(i+1))
for j in range(rows-1, 0, -1):
    print(" "*(rows-j)+'* '*(j))

print("--------SQUARE PATTERN WITH NUMBERS-------")

rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()

print("----------------------------")

word = "Hetvi"
x = ""
for i in word:
    x += i
    print(x)

print("----------------------------")

for row in range(9):
    for col in range(7):
        if col==0 or col==6 or (row==4 and (col>0 and col<6)):
            print("*", end="")
        else:
            print(end=" ")
    print()

print("----------------------------")
n = 10
for i in range(10):
    for j in range(n-i):
        print(j+1, end=" ")
    print()

print("----------------------------")


n = 5
for i in range(n):
    for j in range(n-i):
        print(i+1, end=" ")
    print()

print("----------------------------")

n = 5
for i in range(n):
    for j in range(n-i):
        print(n-i,end=" ")
    print()

print("----------------------------")

n = 5
for i in range(n):
    for j in range(n-i):
        print(n-j,end=" ")
    print()

