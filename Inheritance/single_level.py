class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def prints(self):
        return self.a, self.b
    
class B(A):
    def __init__(self, a, b):
        super().__init__(a, b)

    
obj = B(10,20)
print("from class B", obj.prints())