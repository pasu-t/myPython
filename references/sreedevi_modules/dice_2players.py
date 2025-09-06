# Task -2  , Two players dice game

from random import randint
from time import sleep

# Enter user details, who are authenticated ( The users names are in "users.txt" file)
with open("dice_users.txt","r") as fobj :
    users_data=fobj.readlines()
users=[]
for i in users_data :
    i=i.rstrip("\n")
    users.append(i)
while True :
    playerOne=input("Enter a player name 1 :")
    if  playerOne in users :
        print("Player 1",playerOne," you are a valid player to play game : ")
        break
    else :
        print("Invalid player name.Enter Valid name")
while True :
    playerTwo=input("Enter a player name 2 : ")
    if playerTwo in users :
        print("Player 2",playerTwo," you are a valid player to play game : ")
        break
    else :
        print("Invalid player name.Enter Valid name")

fobj.close()   

# Allow the players to Play 5 rounds the game , each player  can roll two 6-sided dice,


playerOneScore = 0
playerTwoScore = 0

for i in range(5):
    print("Player 1 it's your turn. " )
    print("Type 'roll' to roll two 6-sided dice  ")
    userOneAns1 = input(">>>")
    if  userOneAns1=="roll" :
        userOneInput1=randint(1,6)
        userOneInput2=randint(1,6)
        print("Player 1 rolled dice 1 ", userOneInput1)
        print("Player 1 rolled  dice 2", userOneInput2)
    # If player1  roll is double, then he gets to roll one extra die    
    if  userOneInput1==userOneInput2 :
        print("Congrats! you got one more chance to roll dice again,Type 'roll' to roll the dice1 ")
        userOneAns1 = input(">>>")
        if  userOneAns1=="roll" :
            extra_dice=randint(1,6)
            print("Player 1 rolled dice 1 ", extra_dice)
            playerOneScore=playerOneScore+userOneInput1+userOneInput2+extra_dice
    else :
        playerOneScore=playerOneScore+userOneInput1+userOneInput2
            
    print(" Player 1 round ",i+1,"score is : ",playerOneScore)
    print("Player 2 it's your turn. " )
    print("Type 'roll' to roll two 6-sided dice   ")
    userTwoAns1 =input(">>>")
    if  userTwoAns1=="roll" :
        userTwoInput1=randint(1,6)
        userTwoInput2=randint(1,6)
        print("Player 2 rolled dice 1 ", userTwoInput1)
        print("Player 2 rolled dice 2 ", userTwoInput2)
    # If player2  roll is double, then he gets to roll one extra die  
    if  userTwoInput1==userTwoInput2 :
        print("Congrats! you got one more chance to roll dice again,Type 'roll' to roll the dice1 ")
        userTwoAns1 = input(">>>")
        if  userTwoAns1=="roll" :
            extra_dice=randint(1,6)
            print("Player 2 rolled dice 1 ", extra_dice)
            playerTwoScore=playerTwoScore+userTwoInput1+userTwoInput2+extra_dice
    else :
        playerTwoScore=playerTwoScore+userTwoInput1+userTwoInput2
    print(" Player 2 round ",i+1,"score is : ",playerTwoScore)

# If player1 score is even number,then  add 10 additional points else substract 5 points
if  playerOneScore%2==0 :
          playerOneScore+=10
else :
          playerOneScore-=5
# If player2 score is even number, then add 10 additional points else substract 5 points
if  playerTwoScore%2==0 :
          playerTwoScore+=10
else :
          playerTwoScore-=5

 
print("Player 1 ",playerOne,"Score is : ",playerOneScore)
print("Player 2 ",playerTwo,"Score is : ",playerTwoScore)
fobj=open("winners.txt","a")

if  playerOneScore > playerTwoScore :
          print("Player 1",playerOne,", is the winner!  and his score is : ",playerOneScore)
          fobj.write(playerOne+":"+str(playerOneScore)+"\n")
          fobj.close()
elif  playerOneScore < playerTwoScore :
          print("Player 2",playerTwo," is the winner! and his score is : ",playerTwoScore)
          fobj.write(playerOne+":"+str(playerOneScore)+"\n")
          fobj.close()
# If both players have the same score, then each playerto roll 1 die until someone wins
else :
          while True :
              print("Both players score same.")
              print("Type one more roll to announce winner")
              print("Player 1 it's your turn. " )
              print("Type 'roll' to roll the dice1  ")
              userOneAns1 = input(">>>")
              if  userOneAns1=="roll" :
                  userOneInput1=randint(1,6)
                  print("Player 1 rolled dice 1 ", userOneInput1)
              
              print("Player 2 it's your turn. " )
              print("Type 'roll' to roll the dice1  ")
              userTwoAns1 = input(">>>")
              if  userTwoAns1=="roll" :
                  userTwoInput1=randint(1,6)
                  print("Player 2 rolled dice 1 ", userTwoInput1)
              if  userOneInput1 > userTwoInput2 :
                    print("Player 1 ",playerOne,"is the winner! and his score is : ",playerOneScore)
                    fobj.write(playerOne+":"+str(playerOneScore)+"\n")
                    fobj.close()
                    break
              elif  userOneInput1 < userTwoInput2 :
                    print("Player 2 ",playerTwo,"is the winner and his score is : " ,playerTwoScore)
                    fobj.write(playerTwo+":"+str(playerTwoScore)+"\n")
                    fobj.close()
                    break
              else :
                    continue
# Diplays top five players names and their scores
print("Top five score players list : ")
with open("winners.txt","r") as x :
    recs=x.readlines()
len=len(recs)
if len>5 :
    players=[]
    scores=[]
    for  i  in  recs :
        pname,score=i.rstrip("\n").split(":")
        players.append(pname)
        scores.append(score)
    scores=sorted(list(set(scores)),reverse=True)

    top=[]
    for  i  in  scores[:5] :
        for  j  in  recs :
            j=j.rstrip("\n")
            if  i  in  j :
                top.append(j)
    for  i  in  top :
       print(i)
else :
    for i in recs :
        print(i.rstrip("\n"))
    

            
    

        

    
    
    



                


        
