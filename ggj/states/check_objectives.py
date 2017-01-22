
import select_row
from . import BaseState


class CheckObjectivesState(BaseState):

    def enter(self):
        print('Entering check objectives')
        left, right, old_obj, new_obj = self.game.model.check_objectives()
        if old_obj and new_obj:
            print('Changing objectives!')
            self.game.model_matcher.update_objective(old_obj, new_obj)

        self.game.animation.create(500, None, self.animation_ended)

    def animation_ended(self):
        s = CheckWinConditionState(self.game)
        self.game.state_machine.change_state(s)


class CheckWinConditionState(BaseState):

    def enter(self):
        print('Entering check win')
        self.left, self.right = self.game.model.check_win_conditions()
        self.game.animation.create(500, None, self.animation_ended)

    def animation_ended(self):
        if self.left or self.right:
            s = GameFinishedState(self.game)
        else:
            s = SwitchPlayerState(self.game)
        self.game.state_machine.change_state(s)


class SwitchPlayerState(BaseState):

    def enter(self):
        print('Entering switch player')
        self.game.model.switch_player()
        s = select_row.SelectRowState(self.game)
        self.game.state_machine.change_state(s)


class GameFinishedState(BaseState):

    def enter(self):
        print('Entering game finished')
        # game finished
