import random

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # random number list
wrong_guesses = 0 # wrong guess counter
game_over = False # current game status
random_number = random.choice(number_list) # generates a random number from the list

# list of hangman iterations
hang_man: list[str] = [
    '''
    _____
    |   |
        |
        |
        |
    ''',

    '''
    _____
    |   |
    O   |
        |
        |
    ''',

    '''
    _____
    |   |
    O   |
    |   |
        |
    ''',

    '''
    _____
    |   |
    O   |
   /|\\  |
        |
    ''',

    '''
    _____
    |   |
    O   |
   /|\\  |
   / \\  |
    '''
] # double backslashes are used to tell python to treat the backslash as a character

while game_over == False: # starts a loop to keep asking for guesses until the game is over
    guess = int(input("Enter your guess: "))

    if guess not in number_list: # checks if the guess is in the list
        print("Please enter a number between 1 and 15")
        continue

    if guess == random_number: # checks if the guess is correct
        print("Congratulations!")
        game_over = True

    else: # if the guess is incorrect, it prints the next iteration of hangman and adds 1 to the wrong guesses
        print(hang_man[wrong_guesses])
        wrong_guesses = wrong_guesses + 1

    if wrong_guesses == 5: # if the player has guessed wrong 5 times, the game ends
        print("Game Over!")
        print(f"The number was {random_number}")
        game_over = True