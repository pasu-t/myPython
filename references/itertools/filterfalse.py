import itertools

def lt_2(num):
	if num < 2:
		return True
	return False

numbers = [0,1,2,3]
letters = ['a','b','c','d']
selectors = [True, True, False,True]

# result = filter(lt_2, numbers)
result = itertools.filterfalse(lt_2, numbers)

for item in result:
	print(item)