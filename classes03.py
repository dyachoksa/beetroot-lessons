# class AnimalError(Exception):
#     pass

# try:
#     raise AnimalError()
# except AnimalError:
#     pass

class Animal():
    def __init__(self, name):
        self.name=name

    def print_name(self):
        print(self.name)

    def can_fly(self):
        print(f"I'm {self.name} and I can't fly\nNo")

class Cat(Animal):
    "pass"

class Dog(Animal):
    pass

class Bird(Animal):
    def can_fly(self):
        print(f"I'm {self.name} and I can fly\nYes")

if __name__ == "__main__":
    b = Bird("popuga")
    b.print_name()
    b.can_fly()

    d = Dog("Tag")
    d.print_name()
    d.can_fly()

    c = Cat("Kis")
    c.print_name()
    c.can_fly()
