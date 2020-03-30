import functools

classes = {}


def to_upper(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        return f(*args, **kwargs).upper()
    
    return wrap


def service(cls):
    classes[cls.__name__] = cls
    cls.name = cls.__name__.upper()
    return cls


def create_object(name, *args, **kwargs):
    return classes[name](*args, **kwargs)


@service
class User:
    pass


@service
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return self.full_name

    @to_upper
    def get_first_name(self):
        return self.first_name

    @property
    def full_name(self):
        """A person full name"""
        return "{} {}".format(self.first_name, self.last_name)
    
    @full_name.setter
    def full_name(self, value):
        if len(value) < 5:
            raise ValueError("Min 5 chars")

        fist_name, last_name = value.split()
        self.first_name = fist_name
        self.last_name = last_name
    
    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None


def get_first_name(obj):
    return obj.first_name


if __name__ == "__main__":
    person = create_object("Person", "John", "Doe")
    print(person.full_name)
    print(person.get_first_name())
    print(get_first_name(person))

    for name in ["first_name", "last_name"]:
        print(f"{name}:", getattr(person, name))
    
    # person.full_name = "User Example"
    # print(person.full_name)

    # person.first_name = 123
    # print(person)

    # del person.full_name
    # print(person)

    import pprint
    fancy_print = getattr(pprint, "pprint")
    fancy_print(classes)

    # print(Person.name)
