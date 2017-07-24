import random

CHOICES = ["rock", "Spock", "paper", "lizard", "scissors"]
CHOICE_BY_NUM = {num: choice for num,choice in zip(range(0, 5), CHOICES)}
CHOICE_BY_NAME = {choice: num for num,choice in zip(range(0, 5), CHOICES)}

def num_to_name(num):
    """ Convert numbers 0-4 to their corresponding choice names. """

    return CHOICE_BY_NUM[num]

def name_to_num(name):
    """ Convert choice string to a number between 0 and 4. """

    return CHOICE_BY_NAME[name]

def play(choice):
    """ Simulate a game of Rock/Paper/Scissors/Lizard/Spock. """

    player_num = name_to_num(choice)
    comp_num = random.randrange(0, 5)
    difference = (player_num - comp_num) % 5
    comp_name = num_to_name(comp_num)

    print("Player chooses", choice)
    print("Computer chooses", comp_name)

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
