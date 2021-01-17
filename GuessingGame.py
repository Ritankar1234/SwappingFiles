import random 
print('Number Guessing Game')
number=random.randint(1,9)
chances=0
print('Guess the number between 1 and 9')
while(chances<5):
    guess=int(input('Enter Your Guess'))
    if(guess==number):
        print('Congratulations, You won')
        break
    elif(guess<number):
        print('Your guess was low, Please guess a higher number')
    else:
        print('Your guess was high, Please guess a lower number')
    chances=chances+1
if(chances>=5):
    print('You lost the game')