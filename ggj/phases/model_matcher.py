from pyxit.game_phase import GamePhase
from ..entities import (
    Tube,
    Ball
)
from ..model import Sniffer


class ModelMatcherPhase(GamePhase):

    def __init__(self, game):
        self.game = game
        self.sniffer = Sniffer(self.game.model)

        lt = Tube.left_one(self.game)
        self.left_tube = lt
        self.game.create_entity(lt)

        rt = Tube.right_one(self.game)
        self.right_tube = rt
        self.game.create_entity(rt)

        ball_data = self.sniffer.get_balls()

        for ball, location in ball_data.items():
            if location[0] == 'left tube':
                self.left_tube.position_for(location[1])

    def run_phase(self, entities, delta):
        pass
