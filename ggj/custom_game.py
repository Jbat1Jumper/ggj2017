
from pyxit.game import Game
from .phases import (
    StateMachinePhase,
    EventsPhase
)
from .states import SelectRowState


class CustomGame(Game):

    def __init__(self):
        super(CustomGame, self).__init__()

    def load(self):
        self.events = EventsPhase(self)
        self.state_machine = StateMachinePhase(self, SelectRowState(self))

        self.add_phase(self.events)
        self.add_phase(self.state_machine)
