from itertools import combinations 

def plndrm_count(strng,include_duplicates=True):
    sub_strings =  [strng[x:y] for x, y in combinations(range(len(strng)+1), r = 2)]
    if not include_duplicates:
        sub_strings = list(dict.fromkeys(sub_strings))
    n = 0
    for element in sub_strings:
        if element[::] == element[::-1]:
            n += 1
    print('No.of polindroms:',n)

plndrm_count('abbaoabba', include_duplicates=True)
