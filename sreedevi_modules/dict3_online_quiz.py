# Online Quiz

x={"What is national flower?":['Jasmine','Rose','Lotus','Tulip'],
   "What is national Tree?":['Almond','Banayan','Mango','Neem'],
   "What is national river?":['Ganga','Yamuna','Krishna','Kaveri'],
   "What is national Animal?":['Lion','Tiger','Elephant','Cow'],
   "What is national Fruit?":['Grapes','Mango','Apple','Orange']}
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
