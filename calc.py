def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


operations = {
    "+": add,
    "-": sub,
    "*": mul
}


while True:
    a = int(input("A: "))
    b = int(input("B: "))
    op = input("Math op (+, -, *): ")

    result = operations[op](a, b)
    print("Result:", result)

    if input("Quit? ") == "y":
        break

    print("")
