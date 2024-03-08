print("Enter the value : ")
n = int(input())
a = 0
b = 1
sum = a + b
count = 1
print("Fibonacci series is: ", end=" ")

while (count <= n):
	count += 1
	print(a, end=" ")
	a = b
	b = sum
	sum = a + b

print("--------------------------------")


#using for loop
fib=[0,1]
n=10
for i in range(2,n):
    fib.append(fib[i-1]+fib[i-2])
print(fib)
