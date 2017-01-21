from . import BaseState


class SelectRowState(BaseState):
    def run(self):
        pass

    def enter(self):
        pass

    def on_up_press(self):
        print('pressing up')

    def on_up_release(self):
        print('releasing up')
