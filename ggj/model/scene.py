
import random

from collections import deque


COLORS = (1, 2, 3, 4, 5)
TABLE_WIDTH = 6
TABLE_HEIGTH = 4
TUBE_CAPACITY = 6


class Scene(object):

    def __init__(self):
        self.table = Table()
        self.left_tube = Tube()
        self.right_tube = Tube()
        self.left_magnet = Magnet()
        self.right_magnet = Magnet(left=False)

    def __str__(self):
        l_t = str(self.left_tube).split('\n')
        l_m = str(self.left_magnet).split('\n')
        r_t = str(self.right_tube).split('\n')
        r_m = str(self.right_magnet).split('\n')
        t = str(self.table).split('\n')

        offset = len(l_t) - len(l_m)
        r = ''
        # tube width = 3, magnet width = 2, table width = table.x * 4
        for y in range(self.left_tube.capacity):
            if y >= offset:
                j = y - offset
                line = ' '.join([l_t[y], l_m[j], t[j], r_m[j], r_t[y]])
            else:
                line = ' '.join([l_t[y], ' ' * (2 * 3 + self.table.x * 4) + r_t[y]])
            r += line + '\n'

        return r


class Magnet(object):
    """
    Warning, y argument is counted from 1, while y and current_pos
    attributes are counted from 0.
    """

    def __init__(self, y=TABLE_HEIGTH, left=True):
        self.left = left
        self.y = y - 1
        self.current_pos = y - 1

    def move_up(self):
        if self.current_pos < self.y:
            self.current_pos += 1

    def move_down(self):
        if self.current_pos > 0:
            self.current_pos -= 1

    def __str__(self):
        r = ''
        for i in reversed(range(self.y + 1)):
            if i == self.current_pos:
                r += '|>' if self.left else '<|'
            else:
                r += '| ' if self.left else ' |'
            r += '\n'
        return r[:-1]


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
        for row in reversed(self.matrix):
            s += ' '.join(str(ball) if ball else '(-)' for ball in row) + '\n'
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
        self.balls = deque(None for i in range(capacity))

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
        return '\n'.join('|' + str(self.balls[i] or '(-)') + '|'
                         for i in reversed(range(self.capacity)))
