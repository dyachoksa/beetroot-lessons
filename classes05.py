class Animal:
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Animal name={self.name} age={self.age}>"

    def __str__(self):
        return f"{self.name} (str)"

    def __format__(self, format_spec):
        return f"{self.name} (formatted)"

    def __eq__(self, value):
        if type(value) is str:
            return self.name == value
        
        if isinstance(value, Animal):
            return self.name == value.name
        
        return False
    
    def __add__(self, value):
        if type(value) is not int:
            raise NotImplementedError()

        self.age += value
        
        return self
    
    def say_name(self):
        "Prints animal name"
        print(f"I'm {self.name}")

class Cat(Animal):
    pass

class Dog(Animal):
    pass

cat = Cat("Tom")
dog = Dog("Bull")

# print("Cat is Tom:", cat == Dog("Tom"))
print(repr(cat))

cat += 3
print(repr(cat))

# print(repr(cat))
# print(cat)
# print(f"{cat}")
# print("Cat:", cat)
# cat.say_name()

# print("Dog:")
# dog.say_name()
