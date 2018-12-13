import pygame
import sys

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

        self.sc = None
        self.createScreen(w, h)

        #game info
        self.gameContinues = True
        self.isWin = False
        self.level = 1

        #Player attributes
        self.pl = None
        self.start_x = 0
        self.start_y = 0

        #attributes for enemies
        self.enemies = [None] * 9
        self.enemy_mov = False
        self.enemy_border = []

        #map of the game
        self.map = Map(self, 1)

        #attributes for Q-Learning with incremental learning
        self.learn = QLearning(self)

        self.iter_num = 0
        self.player_max_moves = 100

        self.myfont = pygame.font.SysFont("monospace", 24)

        # render text
        self.lbl_iter_num = None
        self.lbl_max_moves = None

    def createScreen(self, w, h):
        pygame.init()
        self.sc = pygame.display.set_mode([w, h])
        self.sc.fill(Game.white)
        pygame.display.flip()

    #main game functions
    def start(self):

        #draw player, enemies and map
        self.createEnv()
        self.game_loop()

    def game_loop(self):

        self.init_positions()
        self.pl.mov_num = 0

        while self.gameContinues:

            self.sc.fill(Game.white)
            self.check_input()

            self.learn.find_move()

            #self.pl.get_keys()
            #print(self.pl.speed, self.enemies[0].speed)

            self.updateMap()

        self.endGame()

    #functions used while game
    def createEnv(self):

        self.sc.fill(Game.white)

        self.pl = Player(self, "./img/player.jpg", 1)

        for i in range(len(self.enemies)):
            self.enemies[i] = EnemyCircle(self, "./img/enemy.jpg", 2, self.enemy_mov)

    def init_positions(self):

        self.pl.set_pos(self.start_x, self.start_y)

        for i in range(len(self.enemies)):
            self.enemies[i].set_pos(260 + 50 * i, (self.enemy_border[0] + 1 if i % 2 == 0 else self.enemy_border[1] - 15))

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def updateMap(self):
        for e in self.enemies:
            e.move()

        self.map.drawMap()
        self.sc.blit(self.pl.image, self.pl.rect)

        self.lbl_iter_num = self.myfont.render("Iter number: " + str(self.iter_num), 1, Game.black)
        self.lbl_max_moves = self.myfont.render("Max moves: " + str(self.player_max_moves), 1, Game.black)

        self.sc.blit(self.lbl_iter_num, (20, 100))
        self.sc.blit(self.lbl_max_moves, (20, 130))

        pygame.display.update()

    def endGame(self):

        if self.isWin:
            print("Hooorraaaay")
            print("Win after %d iterations" %self.iter_num)
        else:
            #update Q-Learning variabless
            self.iter_num += 1

            if self.iter_num % 5 == 0:
                self.player_max_moves += 5

            if self.iter_num % 50 == 0:
                self.learn.eps /= 2

            #restart the game

            self.gameContinues = True
            self.game_loop()


