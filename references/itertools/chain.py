import itertools

numbers = [0,1,2,3]
letters = ['a','b','c','d']
names = ['pasu', 'thumbu']

combined = itertools.chain(numbers, letters, names)

for item in combined:
	print(item)