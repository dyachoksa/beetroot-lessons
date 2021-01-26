"""
Write a decorator that takes a list of stop words and 
replaces them with * inside the decorated function.

def stop_words(words: list):
    pass

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
"""


def stop_words(words):
    def wrapper(func):
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)

            for word in words:
                res = res.replace(word, "*")

            return res

        return inner

    return wrapper


@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
