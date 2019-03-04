from functools import wraps

def decorator(fn):
    @wraps(fn)
    def wrapFunction(*args, **kwargs):
        print("Invokation before function " + fn.__name__)
        fn(*args, **kwargs)
        print("Invokation after function " + fn.__name__)
    return wrapFunction

@decorator
def my_func():
    print("I am a function")

my_func()