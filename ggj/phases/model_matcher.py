from pyxit.game_phase import GamePhase
from ..entities import (
    Tube,
    Ball
)


class ModelMatcherPhase(GamePhase):

    def __init__(self, game):
        self.game = game

        model = self.game.model

        lt = Tube(self.game, 0, 0)
        self.left_tube = lt
        self.game.create_entity(lt)

        rt = Tube(self.game, 0, 0)
        self.right_tube = rt
        self.game.create_entity(rt)

    def run_phase(self, entities, delta):
        pass
