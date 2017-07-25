from rpslsgame import Game
from funcs import play_round

CHOICES = ["rock", "spock", "paper", "lizard", "scissors"]

def main():
    """ Set up and tear down game logic. """

    newGame = Game()
    newGame.welcome()

    while newGame.in_progress:
        player_choice = input("What is your choice? ").lower()
        print()

        if player_choice in CHOICES:
            play_round(player_choice, CHOICES, newGame)
        else:
            print("I'm sorry, that doesn't seem to be a valid choice.")

        continue_answer = input("Continue playing? ")

        if continue_answer not in ['y', 'yes', 'Yes', 'YES']:
            newGame.finish_game()

if __name__ == "__main__":
    main()
