class triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_triangle(self):
        triangle = self.angle1 + self.angle2 + self.angle3
        if triangle == 180:
            print("Given Values will shape a triangle")
        else:
            print("No, it is not perfect triangle")


t1 = triangle(10,20,30)
t1.check_triangle()