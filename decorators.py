import typing
import functools


def bold(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return "**{}**".format(res)

    return wrapper


def italic(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return "##{}##".format(res)

    return wrapper


@bold
@italic
def greet():
    return "Nice day!"

# greet = bold(italic(greet))

print(greet())


def validate(f: typing.Callable):
    @functools.wraps(f)
    def wrap(**kwargs):
        for arg in f.__annotations__:
            if type(kwargs[arg]) is not f.__annotations__[arg]:
                raise ValueError("Type missmatch: {} <> {}".format(type(kwargs[arg]), f.__annotations__[arg]))

        return f(**kwargs)
    
    return wrap


@validate
def greet(name: str, age: int = 18):
    print(f"Hello, {name}!")


greet(name="Sergey", age=18)
greet(name="Me", age = 21)
