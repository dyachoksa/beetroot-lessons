import math

class ThreeDShape:
    def volume(self):
        return 0

class Shape:
    def __init__(self):
        self.name = "Basic Shape"

    def get_name(self):
        return self.name

    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.name = "Circle"
        self.radius = radius

    def get_name(self):
        return super().get_name()
    
    def area(self):
        return math.pi * (self.radius**2)

    def get_radius(self):
        return self.radius


class Square(Shape):
    def __init__(self, size):
        super().__init__()

        self.name = "Square"
        self.size = size

    def area(self):
        return self.size**2


class Qube(Shape, ThreeDShape):
    def get_name(self):
        return "Qube"

    def area(self):
        return 100
    
    def volume(self):
        return 1000


def get_double_area(obj: Shape):
    return obj.area()*2


def get_double_volume(obj):
    return obj.volume() * 2


basic_shape = Shape()
circle = Circle(10)
square = Square(5)
q = Qube()

# print("Name:", basic_shape.get_name())
# print("Area:", get_double_area(basic_shape))

print("Name:", circle.get_name())
print("Circle area:", get_double_area(circle))
print("Radius:", circle.get_radius())

# print("Name:", square.get_name())
# print("Square area:", get_double_area(square))

# print("Name:", q.get_name())
# print("Square area:", get_double_area(q))

