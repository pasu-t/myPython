import functools
a =[100,200,4,500,15,491,350]
x = functools.reduce(lambda i,j: i if i>j else j , a)
print(x)