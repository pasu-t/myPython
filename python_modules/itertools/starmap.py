import itertools

squares = itertools.starmap(pow, [(0,2),(1,2),(2,2)])
print(list(squares))