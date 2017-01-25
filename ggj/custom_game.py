
from pyxit.game import Game
from phases import (
    StateMachinePhase,
    EventsPhase,
    ModelMatcherPhase,
    RenderPhase,
    AnimationPhase
)
from entities.props import (
    prepare_props,
    create_nahuelito,
    create_background,
    create_foregraund
)
from states import SelectRowState
from model import Model

TILE = 16


class CustomGame(Game):

    def __init__(self):
        super(CustomGame, self).__init__()
        self.tilemap_size = TILE * 21, TILE * 15
        self.screen_size = self.tilemap_size[0] * 3, self.tilemap_size[1] * 3

    def load(self):

        prepare_props(self)

        create_background(self)

        self.initialize()

    def initialize(self):
        self.model = Model()

        self.model_matcher = ModelMatcherPhase(self)
        self.events = EventsPhase(self)
        self.animation = AnimationPhase(self)
        self.state_machine = StateMachinePhase(self, SelectRowState(self))
        self.render = RenderPhase(self, self.screen, self.tilemap_size)

        create_nahuelito(self)

        create_foregraund(self)

        self.add_phase(self.events)
        self.add_phase(self.state_machine)
        self.add_phase(self.model_matcher)
        self.add_phase(self.animation)
        self.add_phase(self.render)

    def restart(self):
        self.running = False
        self.time = 0.0
        self.phases = []
        self.entities = []

        prepare_props(self)

        create_background(self)
        self.initialize()

        self.running = True
