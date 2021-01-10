"""
Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

Create a function which takes as input two dicts with structure 
mentioned above, then computes and returns the total price of stock.
"""


def calculate_stock(in_stock, in_prices):
    total_stock = 0

    for item in in_stock:
        item_total = in_stock[item] * in_prices.get(item, 0)
        total_stock += item_total

    return total_stock


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}

print("Total price in stock:", calculate_stock(stock, prices))
print(stock, prices)

stock["lemon"] = 2
prices["lemon"] = 2.5
print("Total price in stock:", calculate_stock(stock, prices))
print(stock, prices)
