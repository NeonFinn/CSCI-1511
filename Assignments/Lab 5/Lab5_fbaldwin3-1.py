# Finn Baldwin, Dice Roll, 2/7/25

import random
dice = [1, 2, 3, 4, 5, 6]
user_input = ''

while user_input.lower() != 'quit':

    roll1 = random.choice(dice)
    roll2 = random.choice(dice)

    print('--------------------------------------------------')
    print(f'Your total is {roll1 + roll2}. You rolled a {roll1} and a {roll2}!')

    if roll1 + roll2 == 2:
        print('Snake Eyes')
    elif roll1 + roll2 == 3:
        print('Ace Caught a Deuce')
    elif roll1 == 2 and roll2 == 2:
        print('Little Joe from Kokomo')
    elif roll1 + roll2 == 5:
        print('Little Phoebe')
    elif roll1 == 3 and roll2 == 3:
        print('Jimmy Hicks from the Sticks')
    elif roll1 == 6 and roll2 == 1:
        print('Six Ace')
    elif roll1 == 4 and roll2 == 4:
        print('Eighter from Decatur')
    elif roll1 + roll2 == 9:
        print('Nina from Pasadena')
    elif roll1 == 5 and roll2 == 5:
        print('Puppy Paws!')
    elif roll1 == 6 and roll2 == 5:
        print('Six Five No Jive')
    elif roll1 + roll2 == 12:
        print('Boxcars')
    else:
        print('No term for this roll')

    user_input = input('Press enter to roll again or type "quit" to exit: ')

print('You have quit the program.')