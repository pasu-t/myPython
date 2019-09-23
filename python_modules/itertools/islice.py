import itertools

numbers = [0,1,2,3]
letters = ['a','b','c','d']
names = ['pasu', 'thumbu']

# result = itertools.islice(iterable, start, stop, step)
# result = itertools.islice(range(10), 5)

result = itertools.islice(range(10), 2,8,2)

for item in result:
	print(item)