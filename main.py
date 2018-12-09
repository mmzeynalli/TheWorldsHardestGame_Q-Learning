from game import Game
from qLearning import QLearning, Tables

w, h = 1000, 1000

game = Game(w, h)
QL = Tables(w, h)

game.start()
