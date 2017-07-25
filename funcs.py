import random

def play_round(player_choice, options, currGame):
    """ Play a game of Rock/Paper/Scissors/Lizard/Spock with input from a user at the command line. """

    # Compare choices numerically
    player_num = options.index(player_choice)
    computer_num = random.randrange(0, 5)
    difference = (player_num - computer_num) % 5

    # Convert computer choice to string
    computer_choice = options[computer_num].capitalize()

    print("You chose", player_choice.capitalize())
    print("Computer chooses", computer_choice, end="\n\n")

    if difference in [3, 4]:
        currGame.computer_wins(player_choice, computer_choice)
    elif difference in [1, 2]:
        currGame.player_wins(player_choice, computer_choice)
    else:
        currGame.tie_game()

    currGame.show_scoreboard()
