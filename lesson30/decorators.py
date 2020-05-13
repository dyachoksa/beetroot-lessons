from functools import wraps


def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Start execution of {func}")

        ret = func(*args, **kwargs)

        print(f"End execution of {func}")

        return ret

    return wrapper


@debug
def say_hello(name, age=18):
    """Prints greeting"""
    print(f"Hello, {name}! Next year you will be {age+1} years old")

    return "Success"


print(say_hello.__doc__)

msg = say_hello("Alex", 21)
print(msg)
