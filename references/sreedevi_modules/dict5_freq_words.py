# Frequency of words

x='''Johny Johny yes papa
eating sugar no papa
telling lies no papa
open your mouth
ha ha ha'''

x=x.replace("\n"," ")
words=x.split(" ")
print(words)

d1={}

for  i  in  set(words) :
    cnt=words.count(i)
    d1[i]=cnt
print(d1)

*******************************
### Happy Independence Day   ###
*******************************
