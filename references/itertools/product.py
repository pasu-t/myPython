import itertools

number = [0,1,2,3]

result = itertools.product(number, repeat = 4)
# result = itertools.combinations_with_replacement(number, 4)

for item in result:
	print(item)