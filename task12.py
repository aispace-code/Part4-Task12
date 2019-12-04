
# Create a decorator that can decorate arbitrary function logging the call and its parameters.﻿

def MyDecorator(func):
    def wrapper(a, b=1, *args, **kwargs):
        print("argument a: ", a)
        print("argument b: ", b)
        print("argument args: ", args)
        print("argument kwargs: ", *kwargs.values())

        return a + b

    return wrapper

@MyDecorator
def testFunc(a, b=1, *args, **kwargs):
    print('This is my how function looks like ')

testFunc(2, 3, 4, 5, c=6, d=7)
print()
testFunc(2, c=5, d=6)
print()
testFunc(10)