# This is a guess the number game which uses random module

import random
i = 1

print('Hello! What is your name?')
myName = input()
 
number = random.randint(1,20)  # 12

print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while i <=5 :
      
     guess = int(input('Take a guess.'))
         
     if guess < number:
          print('Your guess is too low.')
     elif guess > number:
          print('Your guess is too high.')

     elif guess == number:
          print('Good job, ' + myName + '! You guessed my number in ' + str(i) + ' guesses!')
          break
     i= i + 1
else :
     print('Nope. The number I was thinking of  ' + str(number))





