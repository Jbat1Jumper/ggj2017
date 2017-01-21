from pyxit.game_phase import GamePhase


class StateMachinePhase(GamePhase):

    def __init__(self, game, initial_state):
        self.game = game
        self._current = initial_state

    def current_state(self):
        return self._current

    def change_state(self, new_state):
        self.current_state.exit()
        self.current_state = new_state
        self.change_state.enter()
