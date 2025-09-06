import itertools

with open('test.log') as f:
	header = itertools.islice(f, 3)

	for line in header:
		print(line, end='')