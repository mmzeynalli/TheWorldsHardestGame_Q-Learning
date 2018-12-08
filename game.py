import pygame

from player import Player
from enemy import EnemyCircle
from qLearning import QLearning

black = 0, 0, 0
white = 255, 255, 255


class Game:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.gameContinues = True
        self.level = 1
        self.sc = 0

        self.createScreen(w, h)

    def createScreen(self, w, h):
        pygame.init()
        self.sc = pygame.display.set_mode([w, h])
        self.sc.fill(white)
        pygame.display.flip()

    def start(self):
        p1 = Player(self, "./img/player.jpg",  self.width / 2, self.height / 2, 30)

        enemies = [None] * 4

        for i in range(len(enemies)):
            enemies[i] = EnemyCircle(self.sc, "./img/enemy.jpg", 300, i * 200, 2, True)

        while self.gameContinues:

            self.sc.fill(Player.white)
            p1.checkInput()

            for e in enemies:
                e.move()

            p1.screen.blit(p1.image, p1.rect)

            pygame.display.flip()

