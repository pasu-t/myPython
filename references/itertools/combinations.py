import itertools

letters = ['a','b','c','d']

result = itertools.combinations(letters, 2)

for item in result:
	print(item)