def deco(fun):
    def wrapper():
        print("decorator....")
        return fun
    return wrapper


@deco
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()


