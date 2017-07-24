# First, I define a helper function to convert the numbers from 0 to 4 to the corresponding choice name.
def number_to_name(number):
    if number == 0:
        number_to_name = "rock"
    elif number == 1:
        number_to_name = "Spock"
    elif number == 2:
        number_to_name = "paper"
    elif number == 3:
        number_to_name = "lizard"
    elif number == 4:
        number_to_name = "scissors"
    return number_to_name

# Then, I define a helper function to convert the choice to a number from 0 to 4.
def name_to_number(name):
    if name == "rock":
        name_to_number = 0
    elif name == "Spock":
        name_to_number = 1
    elif name == "paper":
        name_to_number = 2
    elif name == "lizard":
        name_to_number = 3
    elif name == "scissors":
        name_to_number = 4
    return name_to_number

#I have to import the random module to use a random function.
import random

#Now, I define the main function that will simulate a game of RPSLS.
def rpsls(name):
    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)
    difference = (player_number - comp_number) % 5
    comp_name = number_to_name(comp_number)
    print("Player chooses",name)
    print("Computer chooses",comp_name)
    if 3 <= difference <= 4:
        print("Computer wins!")
    elif 1 <= difference <=2:
        print("Player wins!")
    else:
        print("Tie game!")
    return rpsls

#And now, I can test my code by calling my function I just defined.
rpsls("rock")
print("")
rpsls("Spock")
print("")
rpsls("paper")
print("")
rpsls("lizard")
print("")
rpsls("scissors")
