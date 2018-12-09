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
        self.enemies = [None]
        self.enemies_rect = [None]

        self.createScreen(w, h)

    def createScreen(self, w, h):
        pygame.init()
        self.sc = pygame.display.set_mode([w, h])
        self.sc.fill(Game.white)
        pygame.display.flip()

    def start(self):
        
        self.map = Map(self, 1)

        self.pl = Player(self, "./img/player.jpg",  self.width / 2, self.height / 2, 30)
        self.enemies = [None] * 4
          
        for i in range(len(self.enemies)):
            self.enemies[i] = EnemyCircle(self, "./img/enemy.jpg", 300, i * 200, 2, True)
            self.enemies_rect.append(self.enemies[i].rect)

        while self.gameContinues:

            self.sc.fill(Player.white)
            self.pl.checkInput()

            for e in self.enemies:
                e.move()

            self.map.drawMap()

            self.pl.game.sc.blit(self.pl.image, self.pl.rect)

            pygame.display.flip()

