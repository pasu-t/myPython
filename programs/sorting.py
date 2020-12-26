mylist = ["cherry", "orange", "banana", "apple"]
mytuple = ("cherry", "orange", "banana", "apple")
print(id(mylist))
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)
mylist.sort(key=lambda a:a[1]) #sort based on second character
print(mylist)
# mytuple.sort() tuples are immutable
newlist = [("cherry",5), ("orange",19), ("banana",32), ("apple", 10)]
newlist.sort(key=lambda qty:qty[1], reverse=True)
print(newlist)
print(id(mylist))

#use sorted if you dont want to change the original list
print('#'*50)
mylist2 = sorted(mylist)
print(id(mylist),id(mylist2))
print(mylist2)
print('-'*50)
mytuple2 = sorted(mytuple)
print(mytuple2)
print('*'*50)
newlist2 = sorted (newlist,key=lambda a:a[1])
print(newlist2)

