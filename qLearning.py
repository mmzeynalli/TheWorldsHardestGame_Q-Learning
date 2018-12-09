from player import Player

dirs = ["right", "left", "up", "down"]

class Tables:
    def __init__(self, w, h):
        #featural Q-Learning
        self.w = []
        self.f = []

        self.q_value = [[0 for i in range(w)] for j in range(h)]

    def updateTables(self, prevTable):
        print("update")

class QLearning:
    def __init__(self, game):
        self.pl = game.pl
        self.game = game

    def calcNextMove(self):

        p = [None] * len(dirs)

        for i in range(len(dirs)):
            p[i] = Player(self.pl.screen, self.pl.imName, self.pl.x, self.pl.y, self.pl.speed)
            p[i].parent = dirs[1 - i]
            p[i].rec_depth = self.pl.rec_depth + 1

        for i in range(len(dirs)):
            if dirs[i] is not self.pl.parent:
                p[i].move(dirs[i], True)

        if p[0].rec_depth == 10:
            return

        for player in p:
            QL = QLearning(player, self.game, self.map)
            QL.calcNextMove()
