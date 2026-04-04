#A rock paper , scissors game

import random

player = int(input(""" 
===================
Rock Paper Scissors
===================   
                                
1)  '✊'
2)  '✋' 
3)  '✌️' 
4)  '🖖' 
5)  '🦎'          
Pick a number :  """))
print(f'You chose: {player}')

computer = random.randint(1, 3)

if player == computer:
    print("It's a tie!")
elif player == 1 and computer == 3:
    print("You win! Rock beats scissors.")
elif player == 2 and computer == 3:
    print("You lost😔 Scissors cuts paper")
elif player == 3 and computer == 2:
    print("You win!!, Scissors cuts paper")
elif player == 1 and computer == 2:
    print("you lost😔, Paper covers rock.")
elif player == 3 and computer == 1:
    print("You lost😔, Rock crushes Scissors.")
elif player == 3 and computer == 5:
    print("You won!, Rock crushes Lizard")
elif player == 5 and computer == 3:
    print("You won!, Spock smashes scissors")
elif player == 5 and computer == 4:
    print("You won!, Lizard poisons Spock")
elif player == 4 and computer == 5:
    print("You lost😔, Spock smashes scissors")
elif player == 4 and computer == 1:
    print("You won!, Spock vaporizes rock")
elif player == 1 and computer == 4:
    print("You lost😔, Spock vaporizes rock")
elif player == 2 and computer == 4:
    print("You won!, Paper disproves Spock")
elif player == 4 and computer == 2:
    print("You lost😔, Paper disproves Spock")
elif player == 2 and computer == 5:
    print("You lost😔, Lizard eats paper")
elif player == 5 and computer == 2:
    print("You won!, Lizard eats paper")
elif player == 1 and computer == 5:
    print("You lost😔, Lizard eats paper")
elif player == 5 and computer == 1:
    print("You won!, Lizard eats paper")
elif player>3:
    print("Wrong input")