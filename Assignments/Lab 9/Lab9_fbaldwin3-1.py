from coin import Coin

def main():
    player1 = Coin()
    player2 = Coin()

    print("-------------------------------------------------------")
    play = input("Do you want to play? (y/n): ").lower()

    while play == 'y':
        player1.toss()
        player2.toss()

        print(f"Player 1 got {player1.get_sideup()} and Player 2 got {player2.get_sideup()}.")

        if player1.get_sideup() == player2.get_sideup():
            player1.set_amount(1)
            player2.set_amount(-1)
            print("The coins match so Player 1 wins this round.")
        else:
            player1.set_amount(-1)
            player2.set_amount(1)
            print("The coins do not match so Player 2 wins this round.")

        print(f"Player 1 Coins: {player1.get_amount()}")
        print(f"Player 2 Coins: {player2.get_amount()}")

        print("-------------------------------------------------------")

        if player1.get_amount() == 0 or player2.get_amount() == 0:
            print("The game has ended because one player ran out of coins.")
            break

        play = input("Do you want to continue playing? (y/n): ").lower()


    print(f"Player 1 Coins: {player1.get_amount()}")
    print(f"Player 2 Coins: {player2.get_amount()}")

    if player1.get_amount() > player2.get_amount():
        print("Player 1 wins the game!")
        input()
    elif player2.get_amount() > player1.get_amount():
        print("Player 2 wins the game!")
        input()
    else:
        print("It's a tie!")
        input()

main()