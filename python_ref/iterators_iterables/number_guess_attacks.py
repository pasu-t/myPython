def my_range(start):
	current = start
	while True:
		yield current
		current += 1
nums = my_range(1)
for num in nums:
	print(num)

#these kind of behaviour from iterator is useful in attacking passwords etc. as it stores only one value at time
	