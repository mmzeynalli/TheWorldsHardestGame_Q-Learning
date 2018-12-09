import pygame

from player import Player
from enemy import EnemyCircle
from qLearning import QLearning
from map import Map

class Game:

    black = 0, 0, 0
    white = 255, 255, 255

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.gameContinues = True
        self.level = 1
        self.sc = 0

        self.pl = None
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
        
        self.map = Map(self, 1)
        print(self.enemy_mov)

        self.pl = Player(self, "./img/player.jpg", 200, 200 , 3)
        self.enemies = [None] * 9
          
        for i in range(len(self.enemies)):
            self.enemies[i] = EnemyCircle(self, "./img/enemy.jpg", 260 + 50 * i, (self.enemy_border[0] if i % 2 == 0 else self.enemy_border[1] - 15), 2, self.enemy_mov)
            
        while self.gameContinues:
            
            self.sc.fill(Player.white)
            self.pl.checkInput()

            self.updateMap()

    def updateMap(self):
        for e in self.enemies:
            e.move()

        self.map.drawMap()
        self.pl.game.sc.blit(self.pl.image, self.pl.rect)

        pygame.display.flip()

