zip vs itertools.zip_longest:
  -> zip pairs up values untill shortest iterable is exhausted
  -> itertools.zip_longest pair up values until longest iterable. It replaces the value with None for short iterable when it comes to pairing
cycle:
 ->takes in an iterator and cycle over these over and over
repeat:
 ->used for passing in a stream of constant values to a function like map or zip
starmap:
 ->Allows map to pass list of tuples as argument
combinations:
 ->combination of items where order matters
permutations:
 ->combinations of items where order does't  matter
product:
 ->permutations and combinations doesn't allow repeat the values, where product can repeat by passing an argument.
 ->we can do the same using combinations_with_replacement
chain:
 -> chain allows us to chain together iterables, so that it goes through all items in first iterable and after that has been exhausted, it goes through second iterable and so on.
islice:
 -> gives slices of iterable
 -> useful when need piece of information from large files.
compress:
 -> gives values when its corresponding seletor is True
 -> filter uses a function to determine whether something i true or false but with compress those values are just passed in as an iterable
dropwhile:
 ->wait until the True value is returned and then it stops applying filter and returns rest of the iterable
takewhile:
 -> grab all the values that return True and as soon as a value that doesn't return True, then it will just return the values that it has at that point.
 groupby:
  ->go through an iterable and group values based on certain key and then it will return a stream of tuple. tuple consist of the key that the items were grouped on and the second value of tuple contains the iterator that contain all of the items that were grouped by the key.