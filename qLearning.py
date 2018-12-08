from player import Player

dirs = ["right", "left", "up", "down"]


class QLearning:
    def __init__(self, player, game, map):
        self.pl = player
        self.map = map
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


class Tables:
    def __init__(self):
        self.reward = []
        self.t = []
        self.qamma = 0.5

        #featural Q-Learning
        self.w = []
        self.f = []

        self.q_value = []


'''
    def updateTables(self, prevTable):
        for i in range(len(self.w)):
            self.q_value[x][y][action] += self.w[i] * self.f[i]

        for i in range(len(self.t)):
            self.q_value[x][y][action] += self.t * (self.reward + self.qamma * prevTable.q_value)
'''
