Decorators, in the general sense, are functions or classes that wrap around another object, that extend, or decorate the object.

A closure is an anonymous function that refers to its parameters or other variables outside its scope. So basically, decorators uses closures, and not replace them.


call vs init in class:

    The first is used to initialise newly created object, and receives arguments used to do that:

    class Foo:
        def __init__(self, a, b, c):
            # ...

    x = Foo(1, 2, 3) # __init__
    The second implements function call operator.

    class Foo:
        def __call__(self, a, b, c):
            # ...

    x = Foo()
    x(1, 2, 3) # __call__



