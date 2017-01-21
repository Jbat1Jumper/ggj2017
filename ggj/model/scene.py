
import random

from collections import deque


COLORS = (1, 2, 3, 4, 5)
TABLE_WIDTH = 6
TABLE_HEIGTH = 4
TUBE_CAPACITY = 6


class Scene(object):

    def __init__(self, seed=7):
        random.seed(seed)
        self.table = Table(self.seed)
        self.left_tube = Tube()
        self.right_tube = Tube()


class Magnet(object):
    pass


class Table(object):

    def __init__(self, x=TABLE_WIDTH, y=TABLE_HEIGTH):
        self.x, self.y = x, y
        self.matrix = []
        for i in range(y):
            self.matrix.append([])
            for j in range(x):
                self.matrix[i].append(Ball.create_random_ball())

    def remove_from_left(self, y):
        return self.remove_from_xy(0, y)

    def remove_from_right(self, y):
        return self.remove_from_xy(self.x - 1, y)

    def remove_from_xy(self, x, y):
        row = self.matrix[y]
        ball = row[x]
        row = row[x+1:] + [None] + row[:x]
        self.matrix[y] = row
        return ball

    def add_ball_to_xy(self, x, y, ball):
        self.matrix[x][y] = ball

    def __str__(self):
        s = ''
        for row in self.matrix:
            s += ' '.join(str(ball) for ball in row) + '\n'
        return s


class Ball(object):

    def __init__(self, color):
        self.color = color

    @classmethod
    def create_random_ball(cls):
        return cls(random.choice(COLORS))

    def __str__(self):
        return '(' + str(self.color) + ')'


class Tube(object):

    def __init__(self, capacity=TUBE_CAPACITY):
        self.capacity = capacity
        self.balls = deque()

    def add_ball(self, ball):
        self.balls.appendleft(ball)
        if len(self.balls) > self.capacity:
            return self.balls.pop()

    @classmethod
    def get_full_tube(cls, capacity=TUBE_CAPACITY):
        t = cls(capacity)
        for i in range(capacity):
            t.add_ball(Ball.create_random_ball())
        return t

    def __str__(self):
        return '\n'.join('|' + str(ball) + '|' for ball in reversed(self.balls))
