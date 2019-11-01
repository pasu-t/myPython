import itertools

# counter = itertools.repeat('pasu', times=5)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))