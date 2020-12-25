When to use closures?
So what are closures good for?

Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.

When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate and more elegant solution. But when the number of attributes and methods get larger, it's better to implement a class.


When do we have closures?

we have a closure in Python when a nested function references a value in its enclosing scope.
The criteria that must be met to create closure in Python are summarized in the following points.

    We must have a nested function (function inside a function).
    The nested function must refer to a value defined in the enclosing function.
    The enclosing function must return the nested function.