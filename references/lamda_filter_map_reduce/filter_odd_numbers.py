def odd_numbers(i):
	if i%2 == 1:
		return i
x = list(range(1,30))
y = filter(odd_numbers, x)
print(y)
print(list(y))

