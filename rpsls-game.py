from gameclass import RPSLSGame
import time

def main():
    """
    Start a new game of Rock-Paper-Scissors-Lizard-Spock. Control the game logic. After each round, prompt the user if they want to continue playing. If they do, begin another round; if not, end the game.
    """

    newGame = RPSLSGame()

    while newGame.in_progress:
        newGame.get_player_choice()

        if newGame.player_choice in newGame.choices:
            newGame.get_computer_choice()
            time.sleep(1)
            newGame.compare_choices()
            time.sleep(0.5)
            newGame.calculate_result()
            time.sleep(0.5)
            newGame.show_scoreboard()
        else:
            print("I'm sorry, that doesn't seem to be a valid choice.")
            newGame.display_choices()

        continue_playing = input("Continue playing? [y/n] ")
        print("-" * 40)

        if continue_playing not in ['y', 'yes', 'Yes', 'YES']:
            newGame.finish_game()

if __name__ == "__main__":
    main()
