import pygame

class Map:
    def __init__(self, game, level):
        self.level = level
        self.game = game

        self.coor = []
        self.lines = []
        self.readFile(level)

        self.drawMap()

    def readFile(self, lvl):

        name = ""
        name += "./levels/" + "level" + str(lvl) + ".txt"

        f = open(name)

        self.readInfo(f)
        self.parseInput(f)

    def readInfo(self, f):
        self.game.enemy_mov = True if f.readline() is "True" else False
        self.game.enemy_border = (tuple(map(int, f.readline().split(","))))
        f.readline()
        
    def parseInput(self, f):
        for line in f:
            temp = line.split(' ')
            self.coor.append((tuple(map(int, temp[0].split(","))), tuple(map(int, temp[1].split(",")))))

        for l in self.coor:
            print(l)


    def drawMap(self):
        for c in self.coor:
            self.lines.append(pygame.draw.line(self.game.sc, self.game.black, c[0], c[1], 3))

    