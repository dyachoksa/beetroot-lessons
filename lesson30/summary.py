## Variables and data types
a_none = None
a_int = 1
a_huge_int = 1_000_000_000
a_float = 2.33
a_bool = True  # False
a_str = "Hello, world!"
a_list = [1, 2, 3, ["a", "b", "c"]]
a_tuple = ("Man", "Woman", "Other")
a_set = {1, 2, 3}  # set(1, 2, 3)
a_dict = {"a": "Letter A", "b": "Letter B"}

## Print
print("\nTypes:")
print("a_none", a_none)
print("a_int", a_int)
print("a_huge_int", a_huge_int)
print("a_float", a_float)
print("a_bool", a_bool)
print("a_str", a_str)
print("a_list", a_list)
print("a_tuple", a_tuple)
print("a_set", a_set)
print("a_dict", a_dict)

print("\nFormatting:")
name = "Developer"
print(f"Hello, {name}!")
print("Hello, {0}!".format(name))

## Loops
print("\nLoops:")
i = 0
while i < 10:
    print(f"{i} * {i} = {i * i}")
    i += 1

for item in range(1, 10):
    print("*" * item)

## If/else
print("\nIf/else:")
name = "Sergey"
age = int(input("Enter your age: "))

if age > 30:
    print("You are too old!")
elif age > 12:
    print("Teenager!")
else:
    print("Hello, kid!")

## Functions
print("\nFunctions and procedures:")


def hello():
    print("Hello from hello()")


hello()


def greet(name):
    return "Hello, {name}".format(name=name)


greet_str = greet("Sergey")
print(greet_str)


def add(x, amount=10):
    print(f"{x} + {amount} = {x+amount}")


add(5)
add(5, 30)
add(5, amount=20)

## Lists
print("\nLists:")
print(a_list)

a_list[1] = "100"
print("a_list[1]", a_list[1])

print(a_list * 2)

a_list.append("new item")
print(a_list)

## Dicts
print("\nDicts:")
print(a_dict)

print("a_dict['a']", a_dict["a"])
a_dict["a"] = "x"

print(a_dict)

a_dict["d"] = "Letter D"
a_dict[None] = "Value"
a_dict.update(
    {
        "e": "Letter E",
        True: "Boolean True",
        False: "Boolean False",
        (1, 2): "Tuple 1, 2",
    }
)

## Import
print("\nImports:")
import pprint

pprint.pprint(a_dict)

## Exceptions
print("\nExceptions:")

try:
    print(a_list[100])
except IndexError as err:
    print("Got an exception:", err)
finally:
    print("It works!")
