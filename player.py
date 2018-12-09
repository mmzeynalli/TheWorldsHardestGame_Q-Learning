import pygame
import sys

class Player:

    white = 255, 255, 255

    def __init__(self, game, image, x, y, speed):

        self.x, self.y = x, y

        #for smooth movement
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60) / 1000.0

        self.speed = speed
        self.imName = image
        self.game = game

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.setPos(x, y)

        self.move_dir = {"right": (self.speed, 0), "left": (-self.speed, 0),
                        "up": (0, -self.speed), "down": (0, self.speed)}

        #for returning
        self.opposite_dir = {"right": "left", "left": "right", "up": "down", "down": "up"}

    def setPos(self, x, y):
        self.rect = self.rect.move(x, y)
        self.game.sc.blit(self.image, self.rect)

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def get_keys(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.move("left")
        if keys[pygame.K_RIGHT]:
            self.move("right")
        if keys[pygame.K_UP]:
            self.move("up")
        if keys[pygame.K_DOWN]:
            self.move("down")

    def move(self, d):

        #move player and update coordinates
        self.x += self.dt * self.move_dir[d][0]
        self.y += self.dt * self.move_dir[d][1]

        self.rect = self.rect.move(self.move_dir[d])

        #reaching finish
        if self.rect.colliderect(self.game.map.finish):
            self.game.gameContinues = False
            self.game.isWin = True

        #intersection logic with borders
        for line in self.game.map.lines:
            if self.rect.colliderect(line):
                self.rect = self.rect.move(self.move_dir[self.opposite_dir[d]])
