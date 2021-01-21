"""
Implement a class Mathematician which is a helper class for doing math operations on lists

The class doesn't take any attributes and only has methods:
 - square_nums (takes a list of integers and returns the list of squares)
 - remove_positives (takes a list of integers and returns it without positive numbers
 - filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

class Mathematician:
    pass

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
"""


class Mathematician:
    def square_nums(self, values):
        return [x*x for x in values]

    def remove_positives(self, values):
        # result = []
        # for value in values:
        #     if value < 0:
        #         result.append(value)
        # return result

        # return [x for x in values if x < 0]

        return list(filter(lambda x: x < 0, values))

    def filter_leaps(self, values):
        return [value for value in values if value % 4 == 0]


m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
