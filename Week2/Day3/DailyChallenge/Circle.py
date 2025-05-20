import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        else:
            self.radius = diameter / 2
        

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius: {self.radius:.2f}, diameter: {self.diameter:.2f}, area: {self.area:.2f}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)

    def __eq__(self, other):
        return isinstance(other, Circle) and self.radius == other.radius

    def __lt__(self, other):
        return isinstance(other, Circle) and self.radius < other.radius

    def __le__(self, other):
        return isinstance(other, Circle) and self.radius <= other.radius

    def __gt__(self, other):
        return isinstance(other, Circle) and self.radius > other.radius

    def __ge__(self, other):
        return isinstance(other, Circle) and self.radius >= other.radius

    def __repr__(self):
        return f"Circle({self.radius:.2f})"


c1 = Circle (4)
c2 = Circle (10)

print (c1)

c3 = c2 + c1
print(c3)

print (c1 == c2)

print (c1 > Circle (3, 9))

circles = [Circle(2), Circle(5), Circle(13)]
sorted_circles = sorted(circles)
print(sorted_circles) 