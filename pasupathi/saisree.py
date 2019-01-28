print ("WELCOME TO THE GK TEST")
score = 0
flower = input("Question 1: What's our national flower ?? \n A)Jasmine \n B)Rose \n C) Lotus \n D) tulip \nEnter your choice : ")
animal = input("Question 2: What's our national animal ?? \n A)Tiger \n B)Elephant \n C) cat \n D) Deer \nEnter your choice : ")
tree = input("Question 3: What's our national tree ?? \n A) Mango \n B) Banayan \n C) Neem \n D) Almond \nEnter your choice : ")
river = input("Question 4: What's our national river ?? \n A) Ganga \n B) yamuna \n C) Kaveri \n D) Godavari \nEnter your choice : ")
fruit = input("Question 5: What's our national fruit ?? \n A) Grape \n B) Orange \n C)Apple \n D) Mango \nEnter your choice : ")
while flower:
    if flower == "C":
        score=1
    else:
        print("Our national flower is LOTUS !!")
    flower =0
while animal:
    if animal == "A":
        score+=1
    else:
        print("Our national animal is TIGER !!")
    animal = 0
while tree:
    if tree == "B":
        score+=1
    else:
        print("Our national tree is BANYAN !!")
    tree = 0
while river:
    if river == "A":
        score += 1
    else:
        print("Our national river is GANGA !!")
    river =0
while fruit:
    if fruit == "D":
        score += 1
    else:
        print("Our national fruit is MANGO !!")
    fruit = 0
print ("Your Total Score : %d" %(score))
