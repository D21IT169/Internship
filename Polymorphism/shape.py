class Shape:
    def calculatearea():
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculatearea(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculatearea(self):
        return self.length * self.width
        
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculatearea(self):
        return 0.5 * self.base * self.height
    
def print_area(shape):
    print(f"Area of the shape is: {shape.calculatearea()}")


circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

print_area(circle)      # Output: Area of the shape is: 78.5
print_area(rectangle)   # Output: Area of the shape is: 24
print_area(triangle)    # Output: Area of the shape is: 12.0
