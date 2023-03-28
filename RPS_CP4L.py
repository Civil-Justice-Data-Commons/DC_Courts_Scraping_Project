# Code below was taken from ChatGPT, believe it or not.
import random


class Bot:
    def __init__(self):
        self.history = {'R': 0, 'P': 0, 'S': 0}
        self.move = ''

    def update_history(self, opponent_move):
        self.history[opponent_move] += 1

    def choose_move(self):
        total_moves = sum(self.history.values())
        if total_moves == 0:
            self.move = random.choice(['R', 'P', 'S'])
        else:
            opponent_moves = list(self.history.keys())
            opponent_frequency = list(self.history.values())
            if opponent_frequency.count(max(opponent_frequency)) > 1:
                moves = [i for i in range(3) if opponent_frequency[i] == max(opponent_frequency)]
                self.move = opponent_moves[random.choice(moves)]
            else:
                self.move = opponent_moves[opponent_frequency.index(max(opponent_frequency))]
        return self.move

    def learn(self, opponent_move):
        self.update_history(opponent_move)


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0

    def play(self, rounds):
        for i in range(rounds):
            player1_move = self.player1.choose_move()
            player2_move = self.player2.choose_move()

            print(f"Player 1: {player1_move}")
            print(f"Player 2: {player2_move}")

            if player1_move == player2_move:
                print("Tie!")
            elif (player1_move == "R" and player2_move == "S") or (player1_move == "P" and player2_move == "R") or (
                    player1_move == "S" and player2_move == "P"):
                print("Player 1 wins!")
                self.player1_score += 1
                self.player1.learn(player2_move)
                self.player2.learn(player1_move)
            else:
                print("Player 2 wins!")
                self.player2_score += 1
                self.player2.learn(player1_move)
                self.player1.learn(player2_move)

            print(f"Score: Player 1: {self.player1_score}, Player 2: {self.player2_score}\n")


bot1 = Bot()
bot2 = Bot()
game = Game(bot1, bot2)
game.play(10000)
