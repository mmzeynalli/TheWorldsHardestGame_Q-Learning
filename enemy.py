import pygame

class EnemyCircle:

    def __init__(self, game, image, x, y, speed, hor):

        self.x = x
        self.y = y

        self.hor = hor

        self.game = game
        self.speed = speed
        self.imName = image

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.initPos(self.x, self.y)

    def initPos(self, x, y):
        self.rect = self.rect.move(x, y)
        self.game.sc.blit(self.image, self.rect)
        pygame.display.flip()

    def move(self):

        if self.game.pl.rect.colliderect(self.rect):
            self.game.gameContinues = False

        if self.hor:
            self.rect = self.rect.move(self.speed, 0)
            self.x += self.speed
        else:
            self.rect = self.rect.move(0, self.speed)
            self.y += self.speed

        self.game.sc.blit(self.image, self.rect)

        if self.x >= 600 or self.x <= 0:
            self.speed *= -1



