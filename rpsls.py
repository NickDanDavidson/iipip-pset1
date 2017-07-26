from rpslsgame import Game

def main():
    """
    Start a new game of Rock-Paper-Scissors-Lizard-Spock. Control the game logic. After each round, prompt the user if they want to continue playing. If they do, begin another round; if not, end the game.
    """

    newGame = Game()

    while newGame.in_progress:
        newGame.get_player_choice()

        if newGame.player_choice in newGame.choices:
            newGame.get_computer_choice()
            newGame.compare_choices()
            newGame.calculate_result()
            newGame.show_scoreboard()
        else:
            print("I'm sorry, that doesn't seem to be a valid choice.")
            print("You can choose from", newGame.choices)

        continue_playing = input("Continue playing? [y/n] ")

        if continue_playing not in ['y', 'yes', 'Yes', 'YES']:
            newGame.finish_game()

if __name__ == "__main__":
    main()
