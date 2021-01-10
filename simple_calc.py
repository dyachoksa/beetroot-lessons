"""
A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic 
operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) 
and an arbitrary number of arguments (only numbers) as the second parameter.
Then return the sum or product of all the numbers in the arbitrary parameter.

For example:
    the call make_operation(‘+’, 7, 7, 2) should return 16
    the call make_operation(‘-’, 5, 5, -10, -20) should return 30
    the call make_operation(‘*’, 7, 6) should return 42  
"""


def make_operation(operation, *args):
    result = 0

    # print(args)

    if operation == "+":
        for num in args:
            result += num

    elif operation == "-":
        for num in args:
            # result -= num
            result = result - num

    elif operation == '*':
        result = 1
        for num in args:
            result *= num

    elif operation == "/":
        for num in args:
            result *= num

    return result


print("make_operation(‘+’, 7, 7, 2)", make_operation('-', 7, 7, 2))
print("make_operation(‘-’, 5, 5, -10, -20)",
      make_operation('-', 5, 5, -10, -20))
print("make_operation(‘*’, 7, 6)", make_operation('*', 7, 6))

print("make_operation(‘+’, 7, 7, 2, 1, 5, 6, 2, 3, 10)",
      make_operation('+', 7, 7, 2, 1, 5, 6, 2, 3, 10))
