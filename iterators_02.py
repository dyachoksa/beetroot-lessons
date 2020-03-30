import sys
import random


class Lotery:
    def __init__(self):
        self.numbers = list(range(37))

    def __iter__(self):
        return self

    def __next__(self):
        num = random.choice(self.numbers)
        self.numbers.remove(num)
        return num


class Enumerator:
    def __init__(self, data, start=0):
        self.data = data
        self.start = start
        self.current_index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            idx = self.current_index

            self.current_index += 1

            return (self.get_index(idx), self.data[idx])
        except IndexError:
            raise StopIteration
    
    def get_index(self, base):
        return self.start + base


for i, x in Enumerator(["one", "two"], start=2):
    print(i, x)
