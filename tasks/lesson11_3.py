"""
Write a class Product that has three attributes:
 - type
 - name
 - price

Then create a class ProductStore, which will have some Products and 
will operate with all products in the store. All methods, in case 
they can’t perform its action, should raise ValueError with appropriate 
error information.

Tips: Use aggregation/composition concepts while implementing 
the ProductStore class. You can also implement additional classes 
to operate on a certain type of product, etc.s

Also, the ProductStore class must have the following methods:
 - add(product, amount) - adds a specified quantity of a single product
     with a predefined price premium for your store(30 percent)
 - set_discount(identifier, percent, identifier_type=’name’) - adds a discount for 
     all products specified by input identifiers (type or name). The discount 
     must be specified in percentage
 - sell_product(product_name, amount) - removes a particular amount of products 
     from the store if available, in other case raises an error. It also 
     increments income if the sell_product method succeeds.
 - get_income() - returns amount of many earned by ProductStore instance.
 - get_all_products() - returns information about all available products in the store.
 - get_product_info(product_name) - returns a tuple with product name and 
     amount of items in the store.

class Product:
    pass

class ProductStore:
    pass

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product(Food, 'Ramen, 1.5)

s = ProductStore()

s.add(p, 10)
s.add(p2, 300)

s.sell(‘Ramen’, 10)

assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)
"""


class Product:
    def __init__(self, product_type, name, price):
        self.product_type = product_type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = []
        self.income = 0

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Can't add non-Product objects")

        self.products.append({
            "product": product,
            "qty": amount
        })

    def set_discount(self, identifier, percent, identifier_type='name'):
        pass

    def sell_product(self, name, amount):
        for item in self.products:
            if item["product"].name == name:
                left_in_stock = item["qty"] - amount
                if left_in_stock < 0:
                    raise ValueError("Not enought product quantity")

                item["qty"] = left_in_stock
                return True

        raise ValueError("Not product found")

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(x["product"].name, x["qty"]) for x in self.products]

    def get_product_info(self, name):
        for item in self.products:
            if item["product"].name == name:
                return (item["product"].name, item["qty"])

        raise ValueError("Not product found")


print("Welcome to Product Store!")

p = Product("Sport", "Football T-Shirt", 100)
p2 = Product("Food", "Ramen", 1.5)

s = ProductStore()

s.add(p, 10)
s.add(p2, 300)

print("Initial store:")
print(s.get_all_products())

s.sell_product("Ramen", 10)

assert s.get_product_info("Ramen") == ("Ramen", 290)
print("Product was sold successfully")

print("After purchase:")
print(s.get_all_products())
