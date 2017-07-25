class Game:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0
        self.in_progress = True

    def welcome(self):
        print("Welcome to Rock-Paper-Scissors-Lizard-Spock: an extension of the classic Rock-Paper-Scissors.", end="\n\n")
        print("You're playing against the computer.")

    def player_wins(self, p_choice, c_choice):
        print("{0} beats {1}. You win!".format(p_choice.capitalize(), c_choice), end="\n\n")
        self.player_score += 1

    def computer_wins(self, p_choice, c_choice):
        print("{0} beats {1}. Computer wins.".format(c_choice, p_choice.capitalize()), end="\n\n")
        self.computer_score += 1

    def tie_game(self):
        print("It's a tie!", end="\n\n")
        self.tie_score += 1

    def show_scoreboard(self):
        print("Player: {0} | Computer: {1} | Ties: {2}".format(self.player_score, self.computer_score, self.tie_score), end="\n\n")

    def finish_game(self):
        self.in_progress = False
        print("Thanks for playing!")
