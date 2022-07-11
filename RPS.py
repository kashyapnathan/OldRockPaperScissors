import math
import random

userVal = None
passval = False
   
while passval==False:
    
    choice = input('Rock, Paper, or Scissors: ')

    if choice == 'Rock':
        userVal = 0
        passval = True
    elif choice == 'Paper':
        userVal = 1
        passval = True
    elif choice == 'Scissors':
        userVal = 2
        passval=True
    else:
        print('Type yo stuff properly bruv')
        

n = random.randrange(0,3) #0=Rock, 1=Paper, 2=Scissors


if n==0 and userVal == 0:
    print('Tie... Try again')
if n==0 and userVal == 1:
    print('Paper beats Rock: User wins ')
if n==0 and userVal == 2:
    print('Rock beats Scissors: Computer wins ')
if n==1 and userVal == 0:
    print('Paper beats Rock: Computer wins ')
if n==1 and userVal == 1:
    print('Tie... Try again')
if n==1 and userVal == 2:
    print('Scissors beats Paper: User wins ')
if n==2 and userVal == 0:
    print('Rock beats Scissors: User wins ')
if n==2 and userVal == 1:
    print('Scissors beats Paper: Computer wins ')
if n==2 and userVal == 2:
    print('Tie... Try again')


