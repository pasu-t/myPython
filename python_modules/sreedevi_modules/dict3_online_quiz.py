# Online Quiz

key=(3,2,1,2,2)
index=0
score=0

for   i,j  in   x.items() :
    print(i)
    for  n,m  in  enumerate(j) :
        print(n+1,".",m)
    ans=int(input("Enter option : "))
    if  ans==key[index] :
        score=score+1
    index=index+1
print("your score is : ",score)
