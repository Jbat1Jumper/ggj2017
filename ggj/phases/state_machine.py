from pyxit.game_phase import GamePhase


class StateMachinePhase(GamePhase):

    def __init__(self, game, initial_state):
        self.game = game
        self._current = initial_state
        self._current.enter()

    def get_current(self):
        return self._current

    def change_state(self, new_state):
        self._current.exit()
        self._current = new_state
        self._current.enter()
