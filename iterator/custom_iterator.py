class PowTwo:
    
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        
        if self.n <= self.max:              #self.n will increase after each iteration
            result = 2 ** self.n
            self.n += 1                     #increament
            return result
        else:
            raise StopIteration

numbers = PowTwo(4)             #value of max

i = iter(numbers)

print(next(i)) 
print(next(i)) 
print(next(i)) 
print(next(i)) 
print(next(i)) 
print(next(i)) 