from pyxit.game_phase import GamePhase
from pyxit.vec import Vec
from ..entities import (
    Tube,
    Ball,
    Objective,
    Magnet,
    ScoreBar
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
        self.old_ball_data = ball_data

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

        self.left_scorebar = ScoreBar(game, is_left=True,
                                      pos=self.left_scorebar_position())
        self.game.create_entity(self.left_scorebar)
        self.right_scorebar = ScoreBar(game, is_left=False,
                                       pos=self.right_scorebar_position())
        self.game.create_entity(self.right_scorebar)

    def get_current_row_balls(self):
        p = self.sniffer.get_current_magnet_position()
        r = []
        for b, l in self.old_ball_data.items():
            if l[0] == 'table' and l[2] == p:
                r.append(b)
        return r

    def update_positions(self):
        self.update_left_magnet_position()
        self.update_right_magnet_position()
        self.update_ball_positions(self.game.entities)

    def update_left_magnet_position(self):
        new_pos = self.left_magnet_position()
        if self.left_magnet.pos != new_pos:
            self.left_magnet.move(new_pos)

    def update_right_magnet_position(self):
        new_pos = self.right_magnet_position()
        if self.right_magnet.pos != new_pos:
            self.right_magnet.move(new_pos)

    def update_ball_positions(self, entities):
        balls_data = self.sniffer.get_balls()
        for entity in entities:
            if isinstance(entity, Ball):
                location = balls_data[entity.ref]
                new_pos = self.ball_position(location)
                if entity.pos != new_pos:
                    entity.move(new_pos)

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

    def left_scorebar_position(self):
        return Vec(TILE, TILE * 13)

    def right_scorebar_position(self):
        return Vec(TILE * 16, TILE * 13)

    def update_objective(self, old_obj, new_obj):
        for i, ent in enumerate(self.game.entities):
            if isinstance(ent, Objective) and ent.ref == old_obj:
                ent.change_ref(new_obj)
