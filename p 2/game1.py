

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0
        self.tmove = random.choice(moves)
        self.imove = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.imove = my_move
        self.tmove = their_move


class HumanPlayer(Player):
    def move(self):
        PlayerChoice = ['rock', 'paper', 'scissors']
        while PlayerChoice not in moves:
            PlayerChoice = input("Chosie Rock , Paper , Scissors: ").lower()
        if PlayerChoice in ["roxk", "rwck", "rook"]:
            PlayerChoice = "rock"
        elif PlayerChoice in ["pepar", "bebar", "piper"]:
            PlayerChoice = "paper"
        elif PlayerChoice in ["Scessor", "Scizor", "Scissar"]:
            PlayerChoice = "Scissors"
        return PlayerChoice


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def move(self):
        return self.tmove


class CyclePalyer(Player):
    def move(self):
        if self.imove == "paper":
            return ("rock")
        elif self.imove == "rock":
            return ("scissors")
        elif self.imove == "scissors":
            return ("paper")
        return self.imove


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1} Player 2: {move2}")

        if beats(move1, move2):
            self.p1.score += 1
            print("Player 1 Win")
        elif beats(move2, move1):
            self.p2.score += 1
            print("Player 2 Win")
        else:
            print("Tie")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            print(
                f"Player 1: {self.p1.score} and Player2: {self.p2.score}")
        print("Game over!")

        if self.p1.score > self.p2.score:
            print("Player 1 Win this game")
        elif self.p2.score > self.p1.score:
            print("Player 2 Win this game")


if __name__ == '__main__':
    PlayType = ["rocker", "random", "reflect", "cycle"]
    while PlayType not in ["rocker", "random", "reflect", "cycle"]:
        PlayType = input(
            "Pleas Choose what type you want to play against "
            "[rocker , random , reflect , cycle]").lower()
    if PlayType == "rocker":
        game = Game(Player(), HumanPlayer())
    elif PlayType == "random":
        game = Game(RandomPlayer(), HumanPlayer())
    elif PlayType == "reflect":
        game = Game(RandomPlayer(), ReflectPlayer())
    elif PlayType == "cycle":
        game = Game(CyclePalyer(), HumanPlayer())


game.play_game()
