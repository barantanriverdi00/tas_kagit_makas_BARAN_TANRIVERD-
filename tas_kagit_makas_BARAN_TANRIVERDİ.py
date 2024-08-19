import random


def rock_paper_scissors_YOUR_NAME():

    print("Welcome to the Rock, Paper, Scissors Game!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.")
    print("The first to win two rounds wins the game.")
    print("Press 'q' to exit the game.\n")


    options = ["rock", "paper", "scissors"]


    player_wins = 0
    computer_wins = 0


    while True:
        player_wins = 0
        computer_wins = 0
        rounds_played = 0

        print("A new game is starting!")


        while player_wins < 2 and computer_wins < 2:

            player_choice = input("Make your choice (rock, paper, scissors): ").lower()

            if player_choice == 'q':
                print("Exiting the game...")
                return

            if player_choice not in options:
                print("Invalid choice, please try again.")
                continue


            computer_choice = random.choice(options)
            print(f"Computer's choice: {computer_choice}")


            if player_choice == computer_choice:
                print("This round is a tie!")
            elif (player_choice == "rock" and computer_choice == "scissors") or \
                    (player_choice == "paper" and computer_choice == "rock") or \
                    (player_choice == "scissors" and computer_choice == "paper"):
                print("You won this round!")
                player_wins += 1
            else:
                print("The computer won this round!")
                computer_wins += 1

            rounds_played += 1
            print(f"Rounds Played: {rounds_played}, Your Wins: {player_wins}, Computer Wins: {computer_wins}\n")


        if player_wins == 2:
            print("Congratulations, you won the game!")
        else:
            print("The computer won the game!")


        play_again = input("Do you want to play another game? (yes/no): ").lower()


        computer_play_again = random.choice(["yes", "no"])
        print(
            f"The computer {'wants to continue playing' if computer_play_again == 'yes' else 'does not want to continue playing'}.\n")

        if play_again != 'yes' or computer_play_again != 'yes':
            print("The game has ended. See you next time!")
            break



rock_paper_scissors_YOUR_NAME()
