import math
import turtle

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Please provide either radius or diameter to create a Circle.")

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __add__(self, other):
        if isinstance(other, Circle):
            new_radius = self.radius + other.radius
            return Circle(radius=new_radius)
        else:
            raise ValueError("Unsupported operand type. You can only add two Circle instances.")

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            raise ValueError("Unsupported operand type. You can only compare two Circle instances.")

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        else:
            raise ValueError("Unsupported operand type. You can only compare two Circle instances.")

# Test the Circle class
if __name__ == "__main__":
    c1 = Circle(radius=5)
    c2 = Circle(diameter=10)
    c3 = Circle(radius=3)
    c4 = Circle(diameter=8)

    circles = [c1, c2, c3, c4]
    circles.sort()

    for circle in circles:
        print(circle)

    # Bonus:
    turtle.speed(0)
    for circle in circles:
        turtle.circle(circle.radius * 10)  # Scale the radius for visualization
    turtle.done()
