import random

class Game:
    """
    Hold Rock-Paper-Scissors-Lizard-Spock game state and utility functions.

    For reference:
        - Rock beats Scissors and Lizard
        - Spock beats Rock and Scissors
        - Paper beats Spock and Rock
        - Lizard beats Paper and Spock
        - Scissors beats Lizard and Paper

    In other words, using modular arithmetic, a choice wins to the two choices behind it in the list and loses to the two choices ahead of it.
    """

    welcome_message = "\nWelcome to Rock-Paper-Scissors-Lizard-Spock: an extension of the classic Rock-Paper-Scissors."
    game_notices = "You're playing against the computer."
    exit_message = "Thanks for playing!"
    choices = ["rock", "spock", "paper", "lizard", "scissors"]

    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0
        self.in_progress = True
        self.player_choice = ""
        self.computer_choice = ""
        self.welcome_player()


    def welcome_player(self):
        """
        Upon instantiation, print welcome message and game notices.
        """

        print(self.welcome_message, end="\n\n")
        print(self.game_notices)


    def get_player_choice(self):
        """
        Ask the user for input and convert it to lowercase.
        """

        self.player_choice = input("What is your choice? ").lower()
        print()


    def get_computer_choice(self):
        """
        Assign the computer a random selection from the available choices.
        """

        self.computer_choice = self.choices[random.randrange(0, 5)]


    def player_wins(self):
        """
        If player wins, print the result and increment player score.
        """

        print("{0} beats {1}. You win!".format(self.player_choice.capitalize(), self.computer_choice.capitalize()), end="\n\n")
        self.player_score += 1


    def computer_wins(self):
        """
        If computer wins, print the result and increment computer score.
        """

        print("{0} beats {1}. Computer wins.".format(self.computer_choice.capitalize(), self.player_choice.capitalize()), end="\n\n")
        self.computer_score += 1


    def tie_game(self):
        """
        If the game is a tie, print the result and increment tie score.
        """

        print("It's a tie!", end="\n\n")
        self.tie_score += 1


    def show_scoreboard(self):
        """
        Print scoreboard showing current game state.
        """

        print("Player: {0} | Computer: {1} | Ties: {2}".format(self.player_score, self.computer_score, self.tie_score), end="\n\n")


    def compare_choices(self):
        """
        Compare the indexes of the player's and computer's choices in the choices list. Print the choices for reference.
        """

        self.difference = (self.choices.index(self.player_choice) - self.choices.index(self.computer_choice)) % 5

        print("You chose", self.player_choice.capitalize())
        print("Computer chooses", self.computer_choice.capitalize(), end="\n\n")


    def calculate_result(self):
        """
        Use the difference between the player's and computer's choices indexes to calculate the winner. The choices are in a certain order in the list so that if the difference is 1 or 2, the player wins; higher, the computer wins; else it's a tie.
        """

        if self.difference in [3, 4]:
            self.computer_wins()
        elif self.difference in [1, 2]:
            self.player_wins()
        else:
            self.tie_game()


    def finish_game(self):
        """
        To end the game, set the game's in_progress state to False and print exit message.
        """

        self.in_progress = False
        print(self.exit_message, end="\n\n")
