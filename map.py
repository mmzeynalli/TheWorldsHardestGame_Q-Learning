import pygame

class Map:
    def __init__(self, game, level):
        self.level = level
        self.game = game

        self.lines = []
        self.readFile(level)

        self.drawMap()

    def readFile(self, lvl):

        name = ""
        name += "./levels/" + "level" + str(lvl) + ".txt"
        print(name)

        f = open(name)
        self.parseInput(f)

    def parseInput(self, f):
        for line in f:
            temp = line.split(' ')
            
            self.lines.append((tuple(map(int, temp[0].split(","))), tuple(map(int, temp[1].split(",")))))

        for l in self.lines:
            print(l)


    def drawMap(self):
        for l in self.lines:
            pygame.draw.line(self.game.sc, self.game.black, l[0], l[1], 3)

    