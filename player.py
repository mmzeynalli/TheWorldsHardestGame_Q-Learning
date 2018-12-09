import pygame
import sys

class Player:

    white = 255, 255, 255

    def __init__(self, game, image, x, y, speed):

        self.x, self.y = x, y
        self.speed = speed
        self.imName = image
        self.game = game

        self.map = game.map

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.setPos(x, y)

        self.move_dir = {"right": (self.speed, 0), "left": (-self.speed, 0),
                        "up": (0, -self.speed), "down": (0, self.speed)}

        self.opposite_dir = {"right": "left", "left": "right", "up": "down", "down": "up"}

        #for Q-Learning
        self.parent = None
        self.rec_depth = 0

    def setPos(self, x, y):
        self.rect = self.rect.move(x, y)
        self.game.sc.blit(self.image, self.rect)

    def checkInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.move("right", False)
                elif event.key == pygame.K_LEFT:
                    self.move("left", False)
                elif event.key == pygame.K_UP:
                    self.move("up", False)
                elif event.key == pygame.K_DOWN:
                    self.move("down", False)

    def move(self, d, simulation):

        self.x += self.move_dir[d][0]
        self.y += self.move_dir[d][1]

        self.rect = self.rect.move(self.move_dir[d])

        for line in self.game.map.lines:
            if self.rect.colliderect(line):
                self.rect = self.rect.move(self.move_dir[self.opposite_dir[d]])

        if not simulation:
            self.game.sc.fill(Player.white)

        #COLLISION LOGIC
