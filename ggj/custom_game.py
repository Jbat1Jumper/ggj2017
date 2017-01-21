
from pyxit.game import Game
from .phases import (
    StateMachinePhase,
    EventsPhase,
    ModelMatcherPhase,
    RenderPhase
)
from .states import SelectRowState
from .model import Model

TILE = 16


class CustomGame(Game):

    def __init__(self):
        super(CustomGame, self).__init__()
        self.tilemap_size = TILE * 21, TILE * 15
        self.screen_size = self.tilemap_size[0] * 3, self.tilemap_size[1] * 3

    def load(self):
        self.model = Model(seed=7)

        self.events = EventsPhase(self)
        self.state_machine = StateMachinePhase(self, SelectRowState(self))
        self.model_matcher = ModelMatcherPhase(self)
        self.render = RenderPhase(self, self.screen, self.tilemap_size)

        self.add_phase(self.events)
        self.add_phase(self.state_machine)
        self.add_phase(self.model_matcher)
        self.add_phase(self.render)
