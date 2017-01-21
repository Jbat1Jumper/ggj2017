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
        self.game.model.left()

    def on_right_press(self):
        self.game.model.right()

    def on_swap_player_press(self):
        self.game.model.switch_player()
