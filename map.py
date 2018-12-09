import pygame

class Map:
    def __init__(self, game, level):
        self.level = level
        self.game = game

        self.coor = []
        self.lines = []
        self.finish = None

        self.readFile(level)

        self.drawMap()

    def readFile(self, lvl):

        name = ""
        name += "./levels/" + "level" + str(lvl) + ".txt"

        f = open(name)

        self.readInfo(f)
        self.parseInput(f)

    def readInfo(self, f):
        self.game.start_x, self.game.start_y = map(int, f.readline().split(","))
        f.readline()

        self.game.enemy_mov = True if f.readline() is "True" else False
        self.game.enemy_border = (tuple(map(int, f.readline().split(","))))
        f.readline()
        
    def parseInput(self, f):
        for line in f:
            temp = line.split(' ')
            self.coor.append((tuple(map(int, temp[0].split(","))), tuple(map(int, temp[1].split(",")))))


    def drawMap(self):
        for c in self.coor:
            self.lines.append(pygame.draw.line(self.game.sc, self.game.black, c[0], c[1], 3))
        
        self.drawFinish()
    
    def drawFinish(self):
        self.finish = pygame.draw.rect(self.game.sc, (0, 255, 0), [750, 250, 80, 150])


    