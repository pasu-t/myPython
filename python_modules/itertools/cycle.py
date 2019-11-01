import itertools

counter = itertools.cycle([11,12,13])
# counter = itertools.cycle(('on', 'off'))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))