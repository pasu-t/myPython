# States / capitals

x={'AP':'Hyd','TN':'Chennai','KN':'Bangalore','UP':'Lucknow'}

name=input("Enter a state / capital name : ") 

for   i,j  in   x.items() :
    if  i==name :
        print(i,"Capital is :",j)
        break
    elif j==name :
        print(j,"State is : ",i)
        break
else :
    print("Invalid state or capital name.")
    

