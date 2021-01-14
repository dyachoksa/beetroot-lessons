import math

from .shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)

        self.name = "Circle"

    def length(self):
        return 2 * math.pi * self.size
