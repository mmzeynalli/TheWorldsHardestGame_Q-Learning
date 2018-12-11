import pygame

class EnemyCircle:

    def __init__(self, game, image, x, y, speed, hor):

        self.x = x
        self.y = y

        self.hor = hor #bool for moving horizontally or not (vertically)

        self.game = game
        self.speed = speed
        self.imName = image

        self.image = pygame.image.load(image)
        self.w = self.image.get_width()
        self.h = self.image.get_height()

        self.rect = self.image.get_rect()
        self.initPos(self.x, self.y)

    def initPos(self, x, y):
        self.rect = self.rect.move(x, y)
        self.game.sc.blit(self.image, self.rect)
        pygame.display.flip()

    def move(self):

        if self.game.pl.rect.colliderect(self.rect):
            self.game.gameContinues = False
            self.game.learn.q_value_table[str(self.game.pl.x)][str(self.game.pl.y)].update_after_death()

        if self.hor:
            self.rect = self.rect.move(self.speed, 0)
            self.x += self.speed
        else:
            self.rect = self.rect.move(0, self.speed)
            self.y += self.speed

        self.game.sc.blit(self.image, self.rect)
        
        if self.hor and self.x >= self.game.enemy_border[1] or self.x < self.game.enemy_border[0] - self.w:
            self.speed *= -1
        elif (not self.hor) and self.y > self.game.enemy_border[1] - self.h or self.y <= self.game.enemy_border[0]:
            self.speed *= -1



