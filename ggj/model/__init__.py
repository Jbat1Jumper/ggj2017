
import random

from .scene import Scene
from .player import Player
from .sniffer import Sniffer
from .objectives import PatternObjectivesGenerator

NUMBER_OF_OBJECTIVES = 3
PATTERN_LENGTH = 3


class Model(object):

    def __init__(self, seed=7):
        random.seed(seed)

        self.scene = Scene()
        self.left_player = Player()
        self.right_player = Player()

        number, length = NUMBER_OF_OBJECTIVES, PATTERN_LENGTH
        self.objectives_gen = PatternObjectivesGenerator(self, number, length)

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
        if self.ball_from_tube:
            self.scene.table.add_ball_at_the_top(self.ball_from_tube)

    def right(self):
        if self.currently_left:
            pos = self.scene.left_magnet.current_pos
        else:
            pos = self.scene.right_magnet.current_pos
        self.ball_from_table = self.scene.table.remove_from_right(pos)
        self.ball_from_tube = self.scene.right_tube.add_ball(self.ball_from_table)
        if self.ball_from_tube:
            self.scene.table.add_ball_at_the_top(self.ball_from_tube)

    @property
    def objectives(self):
        return self.objectives_gen.objectives

    def switch_player(self):
        self.currently_left = not self.currently_left

    def check_conditions(self):
        result = (False, False)
        for obj in self.objectives:
            if obj.check_conditions(self.scene.left_tube):
                result[0] = True
            if obj.check_conditions(self.scene.right_tube):
                result[1] = True
            if any(result):
                self.objectives_gen.replace_objective(obj)
                break
        return result

    def check_win_conditions(self):
        return self.objective.check_conditions()

    def __str__(self):
        s = 'Conditions: ' + ' | '.join(str(x) for x in self.objectives) + '\n\n'
        return s + str(self.scene)
