"""
Write a Python program to detect the number of local variables declared in a function.
"""


def print_hello(name):
    num = 18
    message = f"Hello, {name}!"

    print("Message:", message)
    print("Local variables:", locals())


print_hello("Sergey")
