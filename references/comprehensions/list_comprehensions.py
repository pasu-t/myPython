#print remainders after dividing squares of numbers with 5
print([(i**2) % 5 for i in range(1,21)])

#print names of age above 60
user_list = [('abc',45),('def',60),('hij', 64),('lmn',61),('opk',62),('qrs',55),('abd',44)]

print([name for name,age in user_list if age > 60])
#names start with a
print([name for name,age in user_list if name.startswith('a')])
print([user[0] for user in user_list if user[0].startswith('a')])

#cartesian product
a = [1,3,5,7]
b = [2,4,6,8]
print([(x,y) for x in a for y in b])

v= [1,4,-3,6]
print([4*x for x in v])