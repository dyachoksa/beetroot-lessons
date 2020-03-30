import functools

class Calculator:
    def __init__(self, name = None):
        self.name = "Calculator"
        if name is not None:
            self.name = name

    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def sum(self, *args):
        return functools.reduce(lambda x, y: x+y, args)
    
    def div(self, a, b):
        if b == 0:
            raise ValueError("Second argument should not be zero")

        return a / b
