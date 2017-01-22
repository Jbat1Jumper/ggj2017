import check_objectives
from . import BaseState


class SelectRowState(BaseState):
    def run(self):
        pass

    def enter(self):
        pass

    def on_up_press(self):
        self.game.model.up()

    def on_down_press(self):
        self.game.model.down()

    def on_left_press(self):
        if self.game.model.left():
            self.change_to_check_condition_state()

    def on_right_press(self):
        if self.game.model.right():
            self.change_to_check_condition_state()

    def on_swap_player_press(self):
        self.game.model.switch_player()

    def change_to_check_condition_state(self):
        s = check_objectives.CheckObjectivesState(self.game)
        self.game.state_machine.change_state(s)
