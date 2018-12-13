import random
from collections import defaultdict

dirs = ["right", "left", "up", "down", "stay"]


class QLearning:
    def __init__(self, game):
        self.pl = game.pl
        self.game = game

        self.eps = 0.64

        #featural Q-Learning
        self.w = [1, -10] #enemies, finish

        self.q_value_table = self.mult_dim_dict(2, QValues, self)

    def mult_dim_dict(self, dim, dict_type, params):
        if dim == 1:
            return defaultdict(lambda: dict_type(params))
        else:
            return defaultdict(lambda: self.mult_dim_dict(dim - 1, dict_type, params))

    def dist_hor(self, obj1, obj2):
        # horizontal distance
        return abs(obj2.x - (obj1.x + obj1.w))

    def dist_ver(self, obj1, obj2):
        # vertical distance
        if abs(obj2.x - obj1.x > 20):
            return 500
        else:
            return abs(obj2.y - obj1.y)

    def find_move(self):
        r = random.random()

        if r < self.eps:
            self.move_randomly()
        else:
            self.move_optimally()

        x, y = self.game.pl.x, self.game.pl.y
        self.q_value_table[x][y].update_value()

    def move_randomly(self):
        i = random.randint(0, len(dirs) - 1)
        self.game.pl.move(dirs[i])

    def move_optimally(self):
        x, y = self.game.pl.x, self.game.pl.y

        self.game.pl.move(self.q_value_table[x][y].find_best_move())


class QValues:
    def __init__(self, QLearning):

        self.QL = QLearning
        self.table = self.QL.q_value_table
        self.pl = self.QL.game.pl

        self.val = []
        self.t = [] #time

        self.sing_val = 0

    def update_value(self):

        if self.pl.mov_num in self.t:
            return

        #if self.sing_val != 0: return

        dist_finish = self.QL.dist_hor(self.QL.game.map.finish, self.pl)
        dist_enemy = self.QL.dist_ver(self.QL.game.enemies[0], self.pl)

        self.t.append(self.pl.mov_num)
        self.val.append(dist_enemy * self.QL.w[0] + dist_finish * self.QL.w[1])

        self.sing_val = dist_enemy * self.QL.w[0] + dist_finish * self.QL.w[1]

    def update_after_death(self):
        if not self.pl.mov_num in self.t:
            self.t.append(self.pl.mov_num)
            self.val.append(-3000)

            #self.sing_val = -3000

    def get_val_at_t(self, mov):
        if mov in self.t:
            return self.val[self.t.index(mov)]
        else:
            return 0

    def find_best_move(self):

        li = []

        for d in dirs:
            x, y = self.pl.move_simulation(d)
            li.append(self.table[x][y].get_val_at_t(self.pl.mov_num + 1))
            #li.append(self.table[x][y].sing_val)

        print("right: %d, left: %d, up: %d, down: %d, stay %d" %(li[0], li[1], li[2], li[3], li[4]))

        maxi = max(li)

        for i in range(len(li)):
            if li[i] == maxi:
                #print("action chosen: ", dirs[i])
                return dirs[i]
