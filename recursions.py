def count(num):
    if num < 0:
        raise ValueError("Can't count negative numbers")

    print(num, end=" ")

    if num == 0:
        return

    count(num-1)


count(10)
