import random

def rand_num():
    for i in range(6):
        yield random.randint(1, 36)

l = list(rand_num())
print(l)


def generate_numbers(how_much=6):
    nums_list = list(range(1, 37))

    random.shuffle(nums_list)
    for n in range(how_much):
        yield nums_list[n]

print(list(generate_numbers()))


def lotery():
    numbers = list(range(1, 37))

    for _ in range(6):
        num = random.choice(numbers)
        yield num
        numbers.remove(num)

print(list(lotery()))
