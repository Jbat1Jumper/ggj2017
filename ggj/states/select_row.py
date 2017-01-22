import check_objectives
from . import BaseState


class SelectRowState(BaseState):
    def run(self):
        pass

    def enter(self):
        pass

    def on_up_left_press(self):
        if self.game.model.currently_left:
            self.game.model.up()

    def on_down_left_press(self):
        if self.game.model.currently_left:
            self.game.model.down()

    def on_left_left_press(self):
        if self.game.model.currently_left and self.game.model.left():
            self.game.model_matcher.left_magnet.push(is_pull=True)
            n = self.game.props['n_izq_cabeza']
            self.animate_nahuelito(n)
            self.change_to_check_condition_state()

    def on_right_left_press(self):
        if self.game.model.currently_left and self.game.model.right():
            self.game.model_matcher.left_magnet.push()
            n = self.game.props['n_der_cabeza']
            self.animate_nahuelito(n)
            self.change_to_check_condition_state()

    def on_up_right_press(self):
        if not self.game.model.currently_left:
            self.game.model.up()

    def on_down_right_press(self):
        if not self.game.model.currently_left:
            self.game.model.down()

    def on_left_right_press(self):
        if not self.game.model.currently_left and self.game.model.left():
            self.game.model_matcher.right_magnet.push()
            n = self.game.props['n_izq_cabeza']
            self.animate_nahuelito(n)
            self.change_to_check_condition_state()

    def on_right_right_press(self):
        if not self.game.model.currently_left and self.game.model.right():
            self.game.model_matcher.right_magnet.push(is_pull=True)
            n = self.game.props['n_der_cabeza']
            self.animate_nahuelito(n)
            self.change_to_check_condition_state()

    def animate_nahuelito(self, n):
        n.change_to('Animation 1', 0)
        max_ms = 500

        def advance(delta):
            n.change_to('Animation 1', delta*max_ms)

        def callback():
            n.change_to('Animation 1', 0)
        self.game.animation.create(max_ms, advance, callback)

    def change_to_check_condition_state(self):
        s = check_objectives.CheckObjectivesState(self.game)
        self.game.state_machine.change_state(s)
