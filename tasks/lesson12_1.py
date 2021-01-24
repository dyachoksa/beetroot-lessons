"""
Method overloading.

Create a base class named Animal with a method called talk and then 
create two subclasses: Dog and Cat, and make their own implementation of 
the method talk be different. For instance, Dog’s can be to print ‘woof woof’, 
while Cat’s can be to print ‘meow’.

Also, create a simple generic function, which takes as input instance of 
a Cat or Dog classes and performs talk method on input parameter. 
"""


class Animal:
    def talk(self):
        print("I can't talk")


class Cat(Animal):
    def talk(self):
        print("Meow!")


class Dog(Animal):
    def talk(self):
        print("Woof, woof!")


def animal_talk(animal):
    animal.talk()


animal_talk(Cat())
animal_talk(Dog())
