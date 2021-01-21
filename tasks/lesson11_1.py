"""
Make a class structure in python representing people at school. 
Make a base class called Person, a class called Student, and 
another one called Teacher. Try to find as many methods and
attributes as you can which belong to different classes, and 
keep in mind which are common and which are not. For example, 
the name should be a Person attribute, while salary should 
only be available to the teacher. 
"""
import random


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    def __init__(self, first_name, last_name, group):
        super().__init__(first_name, last_name)

        self.group = group

    def get_score(self):
        return random.randint(50, 100)


class Teacher(Person):
    def __init__(self, first_name, last_name, email, subjects):
        super().__init__(first_name, last_name)

        self.email = email
        self.subjects = subjects
        self.salary = None

    def set_salary(self, amount):
        self.salary = amount


katrina = Student("Katrina", "Oliver", "1A")
allen = Student("Allen", "Sullivan", "1A")

teacher = Teacher("Paul", "Willis", "paul.willis@example.com",
                  ["Math", "Physics"])

print(katrina.get_full_name(), "scored", katrina.get_score())
print(allen.get_full_name(), "scored", allen.get_score())

teacher.set_salary(1999)
print(teacher.get_full_name(), "salary", teacher.salary)
