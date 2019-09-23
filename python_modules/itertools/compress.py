import itertools

numbers = [0,1,2,3]
letters = ['a','b','c','d']
selectors = [True, True, False,True]

combined = itertools.compress(letters, selectors)

for item in combined:
	print(item)