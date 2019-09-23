import itertools
import operator

numbers = [1,2,3,2,1,0]
letters = ['a','b','c','d']

# result = itertools.accumulate(numbers)
result = itertools.accumulate(numbers, operator.mul)

for item in result:
	print(item)