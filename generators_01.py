import random

def squares(max_num):
    for i in range(1, max_num+1):
        yield i**2

it = squares(10)
print(type(it))
for x in it:
    print(x)