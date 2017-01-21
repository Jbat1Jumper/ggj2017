
from pyxit.game import Game
from .phases import (
    StateMachinePhase,
    EventsPhase,
    ModelMatcherPhase
)
from .states import SelectRowState


class CustomGame(Game):

    def __init__(self):
        super(CustomGame, self).__init__()

    def load(self):
        self.model = None

        self.events = EventsPhase(self)
        self.state_machine = StateMachinePhase(self, SelectRowState(self))
        self.model_matcher = ModelMatcherPhase(self)

        self.add_phase(self.events)
        self.add_phase(self.state_machine)
        self.add_phase(self.model_matcher)
