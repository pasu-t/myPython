import itertools

letters = ['a','b','c','d']
number = [0,1,2,3]

result = itertools.permutations(letters, 2)

for item in result:
	print(item)