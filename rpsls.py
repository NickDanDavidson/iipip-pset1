import random

CHOICES = ["rock", "Spock", "paper", "lizard", "scissors"]

def play(choice):
    """ Simulate a game of Rock/Paper/Scissors/Lizard/Spock. """

    # Compare choices numerically
    player_num = CHOICES.index(choice)
    comp_num = random.randrange(0, 5)
    difference = (player_num - comp_num) % 5

    # Convert computer choice to string
    comp_choice = CHOICES[comp_num]

    print("Player chooses", choice)
    print("Computer chooses", comp_choice)

    if difference in [3, 4]:
        outcome = "Computer wins!"
    elif difference in [1, 2]:
        outcome = "Player wins!"
    else:
        outcome = "Tie game!"

    print(outcome, end="\n\n")

# Simulate rounds of RPSLS
play("rock")
play("Spock")
play("paper")
play("lizard")
play("scissors")
