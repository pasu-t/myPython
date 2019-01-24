# Online Quiz

x={"What is national flower?":{'a':'Jasmine','b':'Rose','c':'Lotus','d':'Tulip'},
   "What is national Tree?":{'a':'Almond','b':'Banayan','c':'Mango','d':'Neem'},
   "What is national river?":{'a':'Ganga','b':'Yamuna','c':'Krishna','d':'Kaveri'},
   "What is national Animal?": {'a':'Lion','b':'Tiger','c':'Elephant','d':'Cow'},
   "What is ntional Fruit?": {'a':'Grapes','b':'Mango','c':'Apple','d':'Orange'}}
key=('c','b','a','b','b')
index=0
score=0
for   i,j  in  x.items() :
    print(i)
    for  n,m  in  j.items() :
        print(n,".",m)
    ans=input("Enter option : ")
    if ans==key[index] :
        score=score+1
    index=index+1
print("Your score is : ",score)
        
#_____________________________________________
# Jumbled Words

x={'cta':['cat','act'],'ohme':'home','edar':['read','dare','dear'],
   'ytponh':'python','ohtmre':'mother'}
score=0
for    i,j  in   x.items() :
    print(i,":",end=" ")
    ans=input()
    if  ans  in  j :
        score+=1
print("your score is : ",score)
    

*******************************
### Happy Independence Day   ###
*******************************
