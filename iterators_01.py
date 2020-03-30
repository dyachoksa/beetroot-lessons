import sys


class Square:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 1
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_num:
            raise StopIteration()

        res = self.current**2

        self.current += 1

        return res

it = Square(10)
# for value in it:
#     print(value)
# print("Mem it:", sys.getsizeof(it))

a_list = list(it)
print(a_list)
# print("Mem list:", sys.getsizeof(a_list))
