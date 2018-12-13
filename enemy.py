import pygame

class EnemyCircle:

    def __init__(self, game, image, speed, hor):

        self.x, self.y = 0, 0

        self.hor = hor #bool for moving horizontally or not (vertically)

        self.game = game
        self.speed = speed
        self.imName = image

        self.image = pygame.image.load(image)
        self.w = self.image.get_width()
        self.h = self.image.get_height()

        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        self.rect = self.rect.move(-self.rect.left, -self.rect.top)
        self.rect = self.rect.move(x, y)

        self.x = self.rect.left
        self.y = self.rect.top

        self.game.sc.blit(self.image, self.rect)

    def move(self):

        if self.game.pl.rect.colliderect(self.rect):
            self.game.gameContinues = False
            self.game.learn.q_value_table[self.game.pl.x][self.game.pl.y].update_after_death()

        if self.hor:
            self.rect = self.rect.move(self.speed, 0)
            self.x = self.rect.left
        else:
            self.rect = self.rect.move(0, self.speed)
            self.y = self.rect.top

        self.game.sc.blit(self.image, self.rect)
        
        if self.hor and self.x >= self.game.enemy_border[1] or self.x < self.game.enemy_border[0] - self.w:
            self.speed *= -1
        elif (not self.hor) and self.y > self.game.enemy_border[1] - self.h or self.y <= self.game.enemy_border[0]:
            self.speed *= -1



