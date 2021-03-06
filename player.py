import pygame


class Player:

    def __init__(self, game, image, speed):

        self.x, self.y = 0, 0

        #to calculate number of moves
        self.mov_num = 0

        #for smooth movement
        #self.clock = pygame.time.Clock()
        #self.dt = 1 #self.clock.tick(60) / 1000.0 #for simulation

        self.speed = speed
        self.imName = image
        self.game = game

        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()

        self.move_dir = {"right": (self.speed, 0), "left": (-self.speed, 0),
                        "up": (0, -self.speed), "down": (0, self.speed), "stay": (0, 0)}

        #for returning
        self.opposite_dir = {"right": "left", "left": "right", "up": "down", "down": "up"}

    def set_pos(self, x, y):
        self.rect = self.rect.move(-self.rect.left, -self.rect.top) #return to 0, 0
        self.rect = self.rect.move(x, y) #come to needed coors

        self.x = self.rect.left
        self.y = self.rect.top

        self.game.sc.blit(self.image, self.rect)

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

        #reaching max move limit
        if self.game.player_max_moves == self.mov_num:
            self.game.gameContinues = False
            return

        #move player and update coordinates
        self.rect = self.rect.move(self.move_dir[d])
        self.x = self.rect.left
        self.y = self.rect.top

        self.mov_num += 1

        #reaching finish
        if self.rect.colliderect(self.game.map.finish):
            self.game.gameContinues = False
            self.game.isWin = True

        #intersection logic with borders
        for line in self.game.map.lines:
            if self.rect.colliderect(line):
                self.rect = self.rect.move(self.move_dir[self.opposite_dir[d]])

    def move_simulation(self, d):
        return self.x + self.move_dir[d][0], self.y + self.move_dir[d][1]

    def mov_back_simulation(self, d):
        return self.move_simulation(self.opposite_dir(d))
