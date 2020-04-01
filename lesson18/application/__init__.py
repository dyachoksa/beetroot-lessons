from .say_welcome import hello

classes = []

class Application:
    def __init__(self, name=None):
        self.name = name or __name__
    
    def run(self):
        hello()
        print(f"Welcome to {self.name}")

        return 0

def get_name():
    return __name__

app = "Welcome"
