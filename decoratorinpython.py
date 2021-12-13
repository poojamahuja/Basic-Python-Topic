# a decorator function
def myDecor(func):
    # inner function like in closures
    def wrapper():
        print("Modified function")
        func()
    return wrapper

# using the decorator function
@myDecor
def myfunc():
    print('Hello!!')

# Calling myfunc()
myfunc()

