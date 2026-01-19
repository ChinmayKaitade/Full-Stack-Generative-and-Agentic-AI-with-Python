from functools import wraps

def my_decorators(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorators
def greet():
    print("Hello from decorators class from chaicode")

greet()
# Before function runs
# Hello from decorators class from chaicode
# After function runs

print(greet.__name__)
# Before function runs
# Hello from decorators class from chaicode
# After function runs
# greet