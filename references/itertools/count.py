import itertools

# counter = itertools.count(start=5, step=5)
# counter = itertools.count(start=5, step=-2.5)
# for count in counter:
# 	print(count)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

data = [100,200,300,400]
# daily_data = list(zip(itertools.count(), data))
daily_data = list(zip(range(10), data))
daily_data2 = list(itertools.zip_longest(range(10), data))
print(daily_data)
print(daily_data2)