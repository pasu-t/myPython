import random

pl1=input("Enter player 1 name : ")
pl2=input("Enter player 2 name : ")
pl1_total=0
pl2_total=0
ans=input("Player1 , type 'roll' to roll two 6 sided  dice : ")
if ans=="roll" :
    x=random.randint(1,6)
    y=random.randint(1,6)
    print("Player 1 dice 1 is : ",x)
    print("Player 1 dice 2 is : ",y)
    pl1_total=x+y
    if  x==y :
        print("Wow! Congrats, you get one more chance to roll dice")
        ans=input("type 'roll' to roll dice : ")
        if ans=="roll" :
             z=random.randint(1,6)
             print("Player 1 extra dice  : ",z)
             pl1_total+=z
    if pl1_total%2==0 :
        pl1_total+=10
    else :
        pl1_total-=5
    print("Player 1",pl1, "total score is : ",pl1_total)

ans=input("Player2 , type 'roll' to roll two 6 sided  dice : ")
if ans=="roll" :
    x=random.randint(1,6)
    y=random.randint(1,6)
    print("Player 2 dice 1 is : ",x)
    print("Player 2 dice 2 is : ",y)
    pl2_total=x+y
    if  x==y :
        print("Wow! Congrats, you get one more chance to roll dice")
        ans=input("type 'roll' to roll dice : ")
        if ans=="roll" :
             z=random.randint(1,6)
             print("Player 2 extra dice  : ",z)
             pl2_total+=z
    if pl2_total%2==0 :
        pl2_total+=10
    else :
        pl2_total-=5
    print("Player 2",pl2, "total score is : ",pl2_total)

if pl1_total>pl2_total :
    print("Player 1",pl1,"won this game.Congratultions.")

elif pl1_total<pl2_total :
    print("Player 2",pl2,"won this game.Congratultions.")
else :
    print("Both players total score is same,pls roll dice again")
    ans=input("Palyer1,type 'roll' to roll dice : ")
    if ans=="roll" :
        x=random.randint(1,6)
        print("Player1,rolled : ",x)
    ans=input("Palyer2,type 'roll' to roll dice : ")
    if ans=="roll" :
        y=random.randint(1,6)
        print("Player2,rolled : ",y)
    if x>y :
        print("Player 1",pl1,"won this game.Congratultions.")
    elif x<y :
        print("Player 2",pl2,"won this game.Congratultions.")
    else :
        print("Oop's. No one won the game.")






        
        







    
            



            
