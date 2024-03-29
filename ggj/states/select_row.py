import animation
from . import BaseState


class SelectRowState(BaseState):
    def run(self):
        pass

    def enter(self):
        self.game.model_matcher.update_data()

    def on_up_left_press(self):
        if self.game.model.currently_left:
            self.game.model.up()
            self.game.model_matcher.update_left_magnet_position()

    def on_down_left_press(self):
        if self.game.model.currently_left:
            self.game.model.down()
            self.game.model_matcher.update_left_magnet_position()

    def on_left_left_press(self):
        if self.game.model.currently_left and self.game.model.left():
            self.game.model_matcher.left_magnet.push(is_pull=True)
            n = self.game.props['n_izq_cabeza']
            self.animate_nahuelito(n)
            self.change_to_animation_state(False)

    def on_right_left_press(self):
        if self.game.model.currently_left and self.game.model.right():
            self.game.model_matcher.left_magnet.push()
            n = self.game.props['n_der_cabeza']
            self.animate_nahuelito(n)
            self.change_to_animation_state(True)

    def on_up_right_press(self):
        if not self.game.model.currently_left:
            self.game.model.up()
            self.game.model_matcher.update_right_magnet_position()

    def on_down_right_press(self):
        if not self.game.model.currently_left:
            self.game.model.down()
            self.game.model_matcher.update_right_magnet_position()

    def on_left_right_press(self):
        if not self.game.model.currently_left and self.game.model.left():
            self.game.model_matcher.right_magnet.push(is_pull=True)
            self.game.model_matcher.right_magnet.push()
            n = self.game.props['n_izq_cabeza']
            self.animate_nahuelito(n)
            self.change_to_animation_state(True)

    def on_right_right_press(self):
        if not self.game.model.currently_left and self.game.model.right():
            self.game.model_matcher.right_magnet.push(is_pull=True)
            n = self.game.props['n_der_cabeza']
            self.animate_nahuelito(n)
            self.change_to_animation_state(False)

    def change_to_animation_state(self, is_push):
        s = animation.BallAnimationState(self.game, is_push)
        self.game.state_machine.change_state(s)

    def animate_nahuelito(self, n):
        n.change_to('Animation 1', 0)
        max_ms = 500

        def advance(delta):
            n.change_to('Animation 1', delta * max_ms)

        def callback():
            n.change_to('Animation 1', 0)
        self.game.animation.create(max_ms, advance, callback)
