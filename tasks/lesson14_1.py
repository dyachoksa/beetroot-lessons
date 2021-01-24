"""
Write a decorator that prints a function with arguments passed to it.

NOTE! It should print the function, not the result of its execution!

For example:
 "add called with 4, 5"

def logger(func):
    pass

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]
"""


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} was called with arguments:", args, kwargs)
        return func(*args, **kwargs)

    return wrapper


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


print(square_all(2, 3, 4))
