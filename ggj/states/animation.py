import check_objectives
from . import BaseState
from entities import Ball
from pyxit.vec import Vec


class BallAnimationState(BaseState):
    def __init__(self, game, pushing):
        super(BallAnimationState, self).__init__(game)
        self.pushing = pushing

    def enter(self):
        create = self.game.animation.create
        a = create(300, self.shake_current_row, self.end_shake)
        a = a.chain(300, None)
        a = a.chain(300, self.move_falling_ball,
                    self.change_to_check_condition_state)

    def shake_current_row(self, percent):
        import math

        balls = self.game.model_matcher.get_current_row_balls()

        for e in self.game.entities:
            if isinstance(e, Ball) and e.ref in balls:
                if e.old_pos_x is None:
                    e.old_pos_x = e.pos.x
                e.pos.x = e.old_pos_x + math.sin(percent * 100) * 3

    def end_shake(self):
        moving_ball = self.game.model_matcher.sniffer.get_ball_from_table()
        bs = []
        mb = None
        for e in self.game.entities:
            if isinstance(e, Ball):
                if e.ref != moving_ball:
                    if e.old_pos_x is not None:
                        e.old_pos_x = None
                        bs.append(e)
                else:
                    e.old_pos_x = None
                    mb = e

        self.game.model_matcher.update_ball_positions(bs)

        if self.game.model.currently_left:
            is_left = True
        else:
            is_left = False
        if self.pushing:
            is_left = not is_left

        if is_left:
            h_pos = 16 * 5
        else:
            h_pos = 16 * 15

        mb.move(Vec(h_pos,
                    mb.pos.y))

    def move_falling_ball(self, percent):
        pass

    def change_to_check_condition_state(self):
        s = check_objectives.CheckObjectivesState(self.game)
        self.game.state_machine.change_state(s)
