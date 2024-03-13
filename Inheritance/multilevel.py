class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def prints(self):
        return self.a, self.b
    
class B(A):
    def __init__(self, a, b):
        super().__init__(a, b)


class C(B):
    def __init__(self, a, b):
        super().__init__(a, b)
    
obj = C(10,20)
print("from class", obj.prints())