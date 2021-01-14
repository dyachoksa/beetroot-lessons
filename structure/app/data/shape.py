import math


class Shape:
    def __init__(self, size):
        self.size = size
        self.name = "Shape"

    def get_name(self):
        return self.name

    def make_double_size(self):
        self.size *= 2

    def length(self):
        return self.size
