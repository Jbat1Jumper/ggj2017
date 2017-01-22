import check_objectives
from . import BaseState


class BallAnimationState(BaseState):
    def enter(self):
        create = self.game.animation.create
        a = create(300, self.shake_current_row)
        a = a.chain(300, self.move_current_row)
        a = a.chain(300, self.move_falling_ball,
                    self.change_to_check_condition_state)

    def shake_current_row(self, percent):

        balls = self.game.model_matcher.get_current_row_balls()

        for b in balls:
            pass

    def move_current_row(self, percent):
        pass

    def move_falling_ball(self, percent):
        pass

    def change_to_check_condition_state(self):
        s = check_objectives.CheckObjectivesState(self.game)
        self.game.state_machine.change_state(s)
