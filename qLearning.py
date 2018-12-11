import random
from collections import defaultdict

dirs = ["right", "left", "up", "down", "stay"]


class QLearning:
    def __init__(self, game):
        self.pl = game.pl
        self.game = game

        self.eps = 0.64

        #featural Q-Learning
        self.w = [1, -2] #enemies, finish

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
        return abs(obj2.y - obj1.y)

    def find_move(self):
        r = random.random()

        if r < self.eps:
            self.move_randomly()
        else:
            self.move_optimally()

        x, y = self.game.pl.x, self.game.pl.y
        self.q_value_table[str(x)][str(y)].update_value()

    def move_randomly(self):
        i = random.randint(0, len(dirs) - 1)
        self.game.pl.move(dirs[i])

    def move_optimally(self):
        x, y = self.game.pl.x, self.game.pl.y

        self.game.pl.move(self.q_value_table[str(x)][str(y)].find_best_move())


class QValues:
    def __init__(self, QLearning):

        self.QL = QLearning
        self.table = self.QL.q_value_table
        self.pl = self.QL.game.pl

        self.val = []
        self.t = [] #time

    def update_value(self):
        dist_finish = self.QL.dist_hor(self.QL.game.map.finish, self.pl)
        dist_enemy = self.QL.dist_ver(self.QL.game.enemies[0], self.pl)

        self.t.append(self.pl.mov_num)
        self.val.append(dist_enemy * self.QL.w[0] + dist_finish * self.QL.w[1])

    def update_after_death(self):
        if not self.pl.mov_num in self.t:
            self.t.append(self.pl.mov)
            self.val.append(-2000)

    def get_val_at_t(self, mov):
        if mov in self.t:
            return self.q[self.t.index(mov)]
        else:
            return 0

    def find_best_move(self):

        l = [0]

        for d in dirs:
            x, y = self.pl.move_simulation(d)
            l.append(self.table[str(x)][str(y)].get_val_at_t(self.pl.mov_num + 1))

        maxi = max(l)

        for i in range(len(l)):
            if l[i] == maxi: return dirs[i]
