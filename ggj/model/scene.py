
import random

from collections import deque


COLORS = {1, 2, 3, 4, 5}


class Scene(object):

    def __init__(self, seed=7):
        random.seed(seed)
        self.table = Table(self.seed)
        self.left_tube = Tube()
        self.right_tube = Tube()


class Table(object):

    def __init__(self, x=6, y=4):
        self.matrix = []
        for i in range(x):
            self.matrix.append([])
            for j in range(y):
                self.matrix[i].append(Ball.create_random_ball())

    def remove_from_xy(self, x, y):
        ball = self.matrix[x][y]
        self.matrix[x][y] = None
        return ball

    def add_ball_to_xy(self, x, y, ball):
        self.matrix[x][y] = ball


class Ball(object):

    def __init__(self, color):
        self.color = color

    @classmethod
    def create_random_ball(cls):
        return cls(random.choice(COLORS))


class Tube(object):

    def __init__(self, capacity=6):
        self.capacity = capacity
        self.balls = deque()

    def add_ball(self, ball):
        self.balls.appendleft(ball)
        if len(deque) > self.capacity:
            return self.balls.pop()
