from pyxit.game_phase import GamePhase
from pyxit.vec import Vec
from ..entities import (
    Tube,
    Ball,
    Objective,
    Magnet
)
from ..model import Sniffer

TILE = 16
DEBUG = False


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

        lm = Magnet(self.game, self.left_magnet_position(),
                    is_left=True)
        self.left_magnet = lm
        self.game.create_entity(lm)

        rm = Magnet(self.game, self.right_magnet_position(),
                    is_left=False)
        self.right_magnet = rm
        self.game.create_entity(rm)

        ball_data = self.sniffer.get_balls()

        if DEBUG:
            for k, v in ball_data.items():
                print(k, ':', v)

        for model_ball, location in ball_data.items():
            pos = self.ball_position(location)
            ball = Ball(self.game, model_ball, pos)
            self.game.create_entity(ball)

        for i, objective in self.sniffer.get_objectives():
            o = Objective(self.game, objective, self.objective_position(i))
            self.game.create_entity(o)

    def run_phase(self, entities, delta):

        balls_data = self.sniffer.get_balls()
        lm_pos = self.left_magnet_position()
        rm_pos = self.right_magnet_position()

        if DEBUG:
            for k, v in balls_data.items():
                print(k, ':', v)

        for entity in entities:
            if isinstance(entity, Ball):
                location = balls_data[entity.ref]
                new_pos = self.ball_position(location)
                entity.move(new_pos)
            elif isinstance(entity, Tube):
                pass
            elif isinstance(entity, Magnet):
                if entity.is_left:
                    entity.move(lm_pos)
                else:
                    entity.move(rm_pos)
            elif isinstance(entity, Objective):
                pass

    def ball_position(self, location):
        if location[0] == 'left tube':
            return self.left_tube.position_for(location[1])
        elif location[0] == 'right tube':
            return self.right_tube.position_for(location[1])
        elif location[0] == 'table':
            return self.table_position_for(location[1], location[2])

    def table_position_for(self, x, y):
        """ Dont know where to put this. Translates (x,y) of
        model matrix to (x,y) in the world """
        return Vec(TILE * 7 + TILE * x,
                   TILE * 9 - TILE * y)

    def left_magnet_position(self):
        i = self.sniffer.get_left_magnet_position()
        return Vec(TILE * 4,
                   TILE * 8 - TILE * i)

    def right_magnet_position(self):
        i = self.sniffer.get_right_magnet_position()
        return Vec(TILE * 15,
                   TILE * 8 - TILE * i)

    def objective_position(self, x):
        return Vec(TILE * 2 + TILE * 2 * x, TILE)

    def update_objective(self, old_obj, new_obj):
        for i, ent in enumerate(self.game.entities):
            if isinstance(ent, Objective) and ent.ref == old_obj:
                ent.change_ref(new_obj)
