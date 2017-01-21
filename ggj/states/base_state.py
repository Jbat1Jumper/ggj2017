

class BaseState(object):

    def __init__(self, game):
        self.game = game

    def run(self):
        pass

    def enter(self):
        pass

    def exit(self):
        pass
