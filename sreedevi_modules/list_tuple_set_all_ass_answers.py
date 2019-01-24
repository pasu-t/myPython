#  WAP Find length without using len() function

x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]

cnt=0
for  i  in  x :
    cnt=cnt+1
print("Lenght : ",cnt)

_________________________________________
#   WAP Find sum of elements without using sum() function

x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]

sum=0
for  i  in  x :
    sum=sum+i
print("sum : ",sum)

_________________________________________
#   WAP Find max element without using max() function

x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]

max=x[0]
for  i  in  x :
    if i>max :
        max=i
print("max : ",max)
________________________________________
#   WAP Find min element without using min() function

x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]

min=x[0]
for  i  in  x :
    if i<min :
        min=i
print("min : ",min)
_________________________________________
#  WAP Accept number and diplay its index without index() method

x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
n=int(input("Enter a number to find inex : "))
if  n  in  x :
    for  i,j  in  enumerate(x) :
        if j==n :
            print(n,"found at ",i,"index")
            break
else :
    print(n," number not found in the list")
_________________________________________
#  WWAP accept a element and count total of no of occureneces
#  without count() method

x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
n=int(input("Enter a number to find inex : "))
cnt=0
for  i  in  x :
    if i==n :
        cnt=cnt+1

print(n," number occured",cnt,"times in the list")
_________________________________________
#  WAP print above list elements in reverse order without
#  using reverse() method

x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
y=[]
for  i  in  x[::-1] :
    y.append(i)

print("Reverse of ",x,"list is :",y)
________________________________________
# WAP store all 1 digit numbers into one list and 2 digit numbers
#    into another list and and 3 digit numbers
#   into another list other remaining numbers into another list display

x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
l1=[]
l2=[]
l3=[]
l4=[]
for  i  in  x:
    if i>=0 and i<=9 : l1.append(i)
    elif i>=10 and i<=99 : l2.append(i)
    elif i>=100 and i<=999 : l3.append(i)
    else : l4.append(i)
   

print "1 digit numbers list : ",l1
print "2 digit numbers list : ",l2
print "3 digit numbers list : ",l3
print "> 3 digit numbers list : ",l4
_________________________________________
# WAP Store even numbers into one list and odd numbers into another list

x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
even_list=[]
odd_list=[]

for  i  in  x:
    if i%2==0 :
        even_list.append(i)
    else :
        odd_list.append(i)
      

print("Even  digit numbers list : ",even_list)
print("Odd digit numbers list : ",odd_list)
_________________________________________
#WAP accept a element and remove the given element from a lits without
#    using remove() method

x=[100,20,503,3,35,600,73,5,200,400,200,56,10,20,9,1801,300,45678,90]
n=int(input("Enter a number to remove : "))
y=[]
if  n  in  x :
    for  i  in  x:
        if i!=n :
            y.append(i)
    x=y
    print("After removing ",n,"number form list :",x)
else :
    print("Given element",n,"not found in a list")
    

________________________________________________________________
#WAP print whatever elements ending with 's' characters

x=['unix','linux','perl','python','java','perl','aws','linux','devops']

for  i  in  x  :
    if i[-1] in "Ss" :
        print i
________________________________________________________________
#WAP program whatever elements begining with vowel charactes.

x=['unix','linux','perl','python','java','perl','aws','linux','devops']

for  i  in  x  :
    if i[0].lower() in "aeiou" :
        print i
________________________________________________________________
#WAP program whatever elements length more than 5 characters.

x=['unix','linux','perl','python','java','perl','aws','linux','devops']

for  i  in  x  :
    if len(i)>5 :
        print i
________________________________________________________________
#WAP delete all duplicate elements.

x=['unix','linux','perl','python','java','perl','aws','linux','devops']

print "Before deleting duplicates ......."
print  x

x=list(set(x))

print "After deleting duplicates ......."
print  x
________________________________________________________________
# WAP display only duplicate elements.

x=['unix','linux','perl','python','java','perl','aws','linux','devops']
y=set([])
for i in x :
    cnt=x.count(i)
    if cnt!=1 :
        y.add(i)
y=list(y)
print y
________________________________________________________________ 
# WAP display only non duplicate elements.

x=['unix','linux','perl','python','java','perl','aws','linux','devops']

for  i  in  x :
    cnt=x.count(i)
    if cnt==1 :
        print i
________________________________________________________________

# WAP take x list and y list common elements and write into z list.

x=['unix','linux','perl','python','java','perl','aws','linux','devops']

y=['c','c++','unix','python','dba','.net','aws']

z=list(set(x) & set(y))
print  z
________________________________________________________________
# WAP take x list and y list non common elements and write into z list.
x=['unix','linux','perl','python','java','perl','aws','linux','devops']

y=['c','c++','unix','python','dba','.net','aws']

z=list(set(x) ^ set(y))
print  z
