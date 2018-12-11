import random
from collections import defaultdict

dirs = ["right", "left", "up", "down", "stay"]


class QLearning:
    def __init__(self, game):
        self.pl = game.pl
        self.game = game

        self.eps = 0.64

        #featural Q-Learning
        self.w = {"enemies": -10, "finish": -10}
        self.f = {"enemies": 0, "finish": 0} #temp values

        self.q_value_table = self.mult_dim_dict(2, QValues, self.game)

    def dist_hor(self, obj1, obj2):
        # horizontal distance
        return obj2.x - (obj1.x + obj1.w)

    def dist_ver(self, obj1, obj2):
        # vertical distance
        return obj2.y - obj1.y

    def find_move(self):
        r = random.random()

        if r <= self.eps:
            self.move_randomly()
        else:
            self.move_optimally()

    def move_randomly(self):
        i = random.randint(0, len(dirs) - 1)
        self.game.pl.move(dirs[i])

    def move_optimally(self):
        x, y = self.game.pl.x, self.game.pl.y

        self.q_value_table[str(x)][str(y)].update_values()

        self.game.pl.move(self.q_value_table[int(x)][int(y)].find_best_move())

    def mult_dim_dict(self, dim, dict_type, params):
        if dim == 1:
            return defaultdict(lambda: dict_type(params))
        else:
            return defaultdict(lambda: self.mult_dim_dict(dim - 1, dict_type, params))


class QValues:
    def __init__(self, game):

        self.game = game

        self.right = 0
        self.left = 0
        self.up = 0
        self.down = 0
        self.stay = 0
        self.t = 0

    def update_values(self):
        for d in dirs:
            next_x, next_y = self.game.pl.move_simulation(d)

    def find_best_move(self):
        maxi = max(self.right, self.left, self.up, self.down, self.stay)

        if maxi == self.right:
            return "right"
        elif maxi == self.left:
            return "left"
        elif maxi == self.up:
            return "up"
        elif maxi == self.down:
            return "down"
        elif maxi == self.stay:
            return "stay"