import math

print("\n")

print("\n")

print("Welcome to the cirlce app,we will tell the perimeter and area of the circle")

print("\n")

class Circle: 

    def __init__(self, radius):

        self.radius = radius

    def area(self):

        return math.pi * self.radius ** 2

    def perimeter(self):

        return 2 * math.pi * self.radius

c = Circle(5)

print("Area:", c.area())

print("\n")

print("Perimeter:", c.perimeter())

print("\n")

print("\n")