class Note:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, {}".format(self.name))


note = Note("Sergey")
note.say_hello()
