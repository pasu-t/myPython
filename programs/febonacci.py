# def febnocci(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     if n > 2:
#         return febnocci(n-2)+febnocci(n-1)

# # for i in range(1,101):
# #     print(i, febnocci(i))

# above is the loop it over and over over....
# febnocci(5) = febnocci(4) + febnocci(3)
#                 febnocci(3)+ febnocci(2) + febnocci(2)+febnocci(1)
#                 .......

# Explicit memoization
# febnocci_cache = {}
# def febnocci(n):
#     if n in febnocci_cache:
#         return febnocci_cache[n]
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     if n > 2:
#         value = febnocci(n-2)+febnocci(n-1)
#         febnocci_cache[n] = value
#         return value

# for i in range(1,101):
#     print(i, febnocci(i))

from functools import lru_cache

@lru_cache(maxsize = 1000)
def febnocci(n):
    if type(n) != int:
        raise TypeError("n must be positive integer")
    if n < 1:
        raise ValueError("n must be positive integer")
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return febnocci(n-2)+febnocci(n-1)

for i in range(1,101):
    print(i, febnocci(i))

# print(febnocci('abc'))
# print(febnocci(-1))



