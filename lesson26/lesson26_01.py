"""
Implement binary search by recursion
"""

import random
import timeit

recursion_iterator = 0


class MyList:
    def __init__(self, lst1: list):
        self.my_list = lst1

    def search_recursion(self, searched_item, left=None, right=None):
        global recursion_iterator
        recursion_iterator += 1
        if left is None:
            left = 0
        if right is None:
            right = len(self.my_list) - 1
        idx = (right + left) // 2
        is_found = False
        if self.my_list[idx] == searched_item:
            return [True, recursion_iterator]
        elif self.my_list[idx] > searched_item:
            if left < idx:
                is_found = self.search_recursion(searched_item, left, idx)[0]
        else:
            if right > idx:
                is_found = self.search_recursion(searched_item, idx + 1, right)[0]
        return [is_found, recursion_iterator]

    def get_fib_number(self, fib_limit):
        fib, prev_fib = 1, 1
        if fib_limit < 3:
            return 1
        while fib < fib_limit:
            fib, prev_fib = fib + prev_fib, fib
        return prev_fib

    def search_fib(self, searched_item):
        left, right = 0, len(self.my_list) - 1
        iter = 0
        while left <= right:
            iter += 1
            idx = self.get_fib_number(right - left) + (left - 1)
            if self.my_list[idx] == searched_item:
                return [True, iter]
            elif left == right:
                return [False, iter]
            elif self.my_list[idx] > searched_item:
                right = idx
            else:
                left = idx + 1
        return [False, iter]

    def search_binary(self, searched_item):
        left, right = 0, len(self.my_list) - 1
        iter = 0
        while left <= right:
            iter += 1
            idx = (right + left) // 2
            if self.my_list[idx] == searched_item:
                return [True, iter]
            elif left == right:
                return [False, iter]
            elif self.my_list[idx] > searched_item:
                right = idx
            else:
                left = idx + 1
        return [False, iter]


def search_recursion(lst1: list, searched_item):
    left, right = 0, len(lst1) - 1
    idx = (right + left) // 2
    is_found = False
    global recursion_iterator
    recursion_iterator += 1
    if lst1[idx] == searched_item:
        return [True, recursion_iterator]
    elif lst1[idx] > searched_item:
        if left < idx:
            is_found = search_recursion(lst1[left:idx], searched_item)[0]
    else:
        if right > idx:
            is_found = search_recursion(lst1[idx + 1 : right + 1], searched_item)[0]
    return [is_found, recursion_iterator]


def search_bin(lst1: list, searched_item):
    left, right = 0, len(lst1) - 1
    iter = 0
    while left <= right:
        iter += 1
        idx = (right + left) // 2
        if lst1[idx] == searched_item:
            return [True, iter]
        elif left == right:
            return [False, iter]
        elif lst1[idx] > searched_item:
            right = idx
        else:
            left = idx + 1
    return [False, iter]


if __name__ == "__main__":
    idx_to_search = 499800

    lst1 = [i for i in range(10000001)]
    c_lst1 = MyList(lst1)

    # print(f"Found by Python IN      : {lst1[idx_to_search] in lst1}")
    # recursion_iterator = 0
    # print(f"Found by FUNC  RECURSION: {search_recursion(lst1, lst1[idx_to_search])}")

    # recursion_iterator = 0
    # print(f"Found by CLASS RECURSION: {c_lst1.search_recursion(lst1[idx_to_search])}")

    # print(f"Found by CLASS FIBONACCI: {c_lst1.search_fib(lst1[idx_to_search])}")
    # print(f"Found by CLASS BINARY   : {c_lst1.search_binary(lst1[idx_to_search])}")
    # print(f"Found by FUNC BINARY    : {search_bin(lst1, lst1[idx_to_search])}")

    to_search = 999999

    print(
        f"Python search     : {timeit.timeit('to_search in lst1', globals=globals(), number=10):.7f}"
    )
    print(
        f"Recursion by FUNC : {timeit.timeit('recursion_iterator=0;search_recursion(lst1, to_search)', globals=globals(), number=10):.7f}"
    )
    print(
        f"Recursion by CLASS: {timeit.timeit('recursion_iterator=0;c_lst1.search_recursion(to_search)', globals=globals(), number=10):.7f}"
    )
    print(
        f"Fibonacci by CLASS: {timeit.timeit('c_lst1.search_fib(to_search)', globals=globals(), number=10):.7f}"
    )
    print(
        f"Binary by CLASS   : {timeit.timeit('c_lst1.search_binary(to_search)', globals=globals(), number=10):.7f}"
    )
    timer = timeit.timeit("search_bin(lst1, to_search)", globals=globals(), number=10)
    print("Binary by FUNC    : {:.7f}".format(timer))
