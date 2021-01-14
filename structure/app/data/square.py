from .shape import Shape


class Square(Shape):
    def __init__(self, radius):
        super().__init__(radius)

        self.name = "Square"

    def length(self):
        return 4 * self.size

    def make_zero(self):
        self.size = 0
