import random

CHOICES = ["rock", "spock", "paper", "lizard", "scissors"]

def play_round(player_choice):
    """ Play a game of Rock/Paper/Scissors/Lizard/Spock with input from a user at the command line. """

    global player_score, computer_score, tie_score, game_in_progress

    # Compare choices numerically
    player_num = CHOICES.index(player_choice)
    comp_num = random.randrange(0, 5)
    difference = (player_num - comp_num) % 5

    # Convert computer choice to string
    comp_choice = CHOICES[comp_num].capitalize()

    print("You chose", player_choice.capitalize())
    print("Computer chooses", comp_choice, end="\n\n")

    if difference in [3, 4]:
        outcome = "{0} beats {1}. Computer wins.".format(comp_choice, player_choice.capitalize())
        computer_score += 1
    elif difference in [1, 2]:
        outcome = "{0} beats {1}. You win!".format(player_choice.capitalize(), comp_choice)
        player_score += 1
    else:
        outcome = "It's a tie!"
        tie_score += 1

    game_score = "Player: {!s} | Computer: {!s} | Ties: {!s}".format(player_score, computer_score, tie_score)

    print(outcome, end="\n\n")
    print(game_score, end="\n\n")

def main():
    """ Set up and tear down game logic. """

    global player_score, computer_score, tie_score, game_in_progress
    game_in_progress = True
    player_score = 0
    computer_score = 0
    tie_score = 0

    print("Welcome to Rock-Paper-Scissors-Lizard-Spock: an extension of the classic Rock-Paper-Scissors.", end="\n\n")
    print("You're playing against the computer.")

    while game_in_progress:
        player_choice = input("What is your choice? ")
        player_choice = player_choice.lower()

        print()

        if player_choice in CHOICES:
            play_round(player_choice)
        else:
            print("I'm sorry, that doesn't seem to be a valid choice.")

        continue_answer = input("Continue playing? ")

        if continue_answer not in ['y', 'yes', 'Yes', 'YES']:
            game_in_progress = False
            print("Thanks for playing!")

if __name__ == "__main__":
    main()
