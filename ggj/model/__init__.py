
import random

from .scene import Scene
from .player import Player
from .sniffer import Sniffer


class Model(object):

    def __init__(self, seed=7):
        random.seed(seed)

        self.scene = Scene()
        self.left_player = Player()
        self.right_player = Player()

        # Random?
        self.currently_left = True

    def up(self):
        if self.currently_left:
            self.scene.left_magnet.move_up()
        else:
            self.scene.right_magnet.move_up()

    def down(self):
        if self.currently_left:
            self.scene.left_magnet.move_down()
        else:
            self.scene.right_magnet.move_down()

    def left(self):
        if self.currently_left:
            pos = self.scene.left_magnet.current_pos
        else:
            pos = self.scene.right_magnet.current_pos
        self.ball_from_table = self.scene.table.remove_from_left(pos)
        self.ball_from_tube = self.scene.left_tube.add_ball(self.ball_from_table)

    def right(self):
        if self.currently_left:
            pos = self.scene.left_magnet.current_pos
        else:
            pos = self.scene.right_magnet.current_pos
        self.ball_from_table = self.scene.table.remove_from_right(pos)
        self.ball_from_tube = self.scene.right_tube.add_ball(self.ball_from_tube)

    def switch_player(self):
        self.currently_left = not self.currently_left
