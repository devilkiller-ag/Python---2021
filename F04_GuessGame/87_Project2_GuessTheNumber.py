import random

randNum = random.randint(1, 100)
guess = 0

print('Welcome to the game og Guess the Number...')
print('I am thinking about a number between 1 and 100. Can you guess it!')
print('Remember You Will Only Get Maximum 20 Chances.')

while(True):
    guess += 1
    usrInput = int(input('Guess the number: '))

    if(usrInput == randNum):
        print(f'You Gussed It Right. The Number I was thinking about is {randNum}.')
        print(f'You took {guess} number of chances to guess it.')
        break;
    elif(usrInput > randNum):
        print(f'Your Guess is Too High! Try something low.')
    else:
        print(f'Your Guess is Too low! Try something high.')
    
    if(guess > 20):
        print("It looks you will not be able to guess the number I was thinking about in this era.")
        
with open('GuessGame\hiscore.txt') as f:
    hiscore = f.read()

if hiscore == '':
    with open('GuessGame\hiscore.txt', 'w') as f:
        f.write(str(guess))

elif int(hiscore) <  guess :
    print('You just broke the lowest number of chances taken to guess the correct number I was thinking about in previous gameplays.')
    with open('GuessGame\hiscore.txt', 'w') as f:
        f.write(str(guess))
