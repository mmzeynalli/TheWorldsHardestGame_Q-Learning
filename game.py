import pygame

from player import Player
from enemy import EnemyCircle
from qLearning import QLearning
from map import Map

class Game:

    black = 0, 0, 0
    white = 255, 255, 255

    def __init__(self, w, h):

        #screen sizes
        self.width = w
        self.height = h

        #game info
        self.gameContinues = True
        self.isWin = False
        self.level = 1
        self.sc = 0

        #Player attributes
        self.pl = None
        self.start_x = 0
        self.start_y = 0

        #map of the game
        self.map = None

        #attributes for enemies
        self.enemies = [None]
        self.enemy_mov = False
        self.enemy_border = []

        self.createScreen(w, h)

    def createScreen(self, w, h):
        pygame.init()
        self.sc = pygame.display.set_mode([w, h])
        self.sc.fill(Game.white)
        pygame.display.flip()

    def start(self):
        
        #draw player, enemies and map
        self.createEnv()

        while self.gameContinues:
            
            self.sc.fill(Player.white)
            self.pl.check_input()
            self.pl.get_keys()

            self.updateMap()

        self.endGame()

    def updateMap(self):
        for e in self.enemies:
            e.move()

        self.map.drawMap()
        self.pl.game.sc.blit(self.pl.image, self.pl.rect)

        pygame.display.flip()

    def createEnv(self):

        self.sc.fill(Player.white)

        self.map = Map(self, 1)
        self.pl = Player(self, "./img/player.jpg", self.start_x, self.start_y , 2)
        self.enemies = [None] * 9
          
        for i in range(len(self.enemies)):
            self.enemies[i] = EnemyCircle(self, "./img/enemy.jpg", 260 + 50 * i, (self.enemy_border[0] if i % 2 == 0 else self.enemy_border[1] - 15), 1, self.enemy_mov)
            

    def endGame(self):
        if self.isWin:
            print("Hooorraaaay")
        else: #restart the game
            self.createEnv()
            self.gameContinues = True
            self.start()


