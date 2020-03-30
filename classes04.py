class Animal:
    def __init__(self):
        self.name = 'Animal'

    def print_name(self):
        return self.name

    def can_fly(self):
        return False

class Cat(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name

class Bird(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def can_fly(self):
        return True

my_cat = Cat('CatName')
print(my_cat.print_name())
print(my_cat.can_fly())

my_dog = Dog('DogName')
print(my_dog.print_name())
print(my_dog.can_fly())

my_bird = Bird('BirdName')
print(my_bird.print_name())
print(my_bird.can_fly())