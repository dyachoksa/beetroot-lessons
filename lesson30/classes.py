class Student:
    count = 0

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

        Student.count += 1

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Student name={self.name} age={self.age}>"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def greet(self):
        return "Hello. I'm {} and I'm {} years old".format(self.get_name(), self.age)


student = Student("Alex")
student.set_age(21)

print(student)
print(repr(student))
print(student.greet())

anna = Student("Anna", 19)
print(repr(anna))

print("Total students:", Student.count)
