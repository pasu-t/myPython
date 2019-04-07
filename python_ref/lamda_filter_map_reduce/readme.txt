lamda function:
-->lamda is a keyword which defines one line statement function without a name
-->Used in higher-order functions where functions are passed as arguments in other function
--> use cases : map, filter uses this lamda
Syntax:
lamda variable : expression

====================================================================================================================
filter()
-->The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
** filter removes : None, False and 0
Syntax:
filter(function, sequence)
Parameters:
  function: function that tests if each element of a sequence true or not.
  sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.
Retruns: returns an iterator that is already filtered.

====================================================================================================================
map()
-->map() function returns a list of the results after applying the given function to each item of a given iterable
syntax:

map(function, iter)
function : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

====================================================================================================================
reduce()
-->The reduce() function accepts a function and a sequence and returns a single value calculated as follows:
      Initially, the function is called with the first two items from the sequence and the result is returned.
      The function is then called again with the result obtained in step 1 and the next value in the sequence. This process keeps repeating until there are items in the sequence.

Syntax:

reduce (function, iterable [, initializer])
function: A function of two arguments.
iterable: An iterable sequence.
initializer: Value placed before the iterable; default value if iterable is empty.
-->When the initial value is provided, the function is called with the initial value and the first item from the sequence.