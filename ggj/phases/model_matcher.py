from pyxit.game_phase import GamePhase
from pyxit.vec import Vec
from ..entities import (
    Tube,
    Ball
)
from ..model import Sniffer

TILE = 16
DEBUG = True


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

        if DEBUG:
            for k, v in ball_data.items():
                print(k, ':', v)

        for model_ball, location in ball_data.items():
            if location[0] == 'left tube':
                pos = self.left_tube.position_for(location[1])
            elif location[0] == 'right tube':
                pos = self.right_tube.position_for(location[1])
            elif location[0] == 'table':
                pos = self.table_position_for(location[1], location[2])

            ball = Ball(self.game, model_ball, pos)
            self.game.create_entity(ball)

    def run_phase(self, entities, delta):
        pass

    def table_position_for(self, x, y):
        """ Dont know where to put this. Translates (x,y) of
        model matrix to (x,y) in the world """
        return Vec(TILE * 7 + TILE * x,
                   TILE * 6 + TILE * y)
