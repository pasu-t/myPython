import functools
x = functools.reduce(lambda i,j: i*j , range(1,6) )
print(x)