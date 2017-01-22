from pyxit.entity import Entity
from pyxit.vec import Vec
import pygame as pg

TILE = 16


class Tube(Entity):

    @classmethod
    def left_one(cls, game):
        t = cls(game, 16, 80)
        t.is_left = True
        t.body_h_offset = TILE * 1
        return t

    @classmethod
    def right_one(cls, game):
        t = cls(game, 240, 80)
        t.is_left = False
        t.body_h_offset = TILE * 3
        return t

    def position_for(self, index):
        v_offset = TILE * 6
        return Vec(self.pos.x + self.body_h_offset,
                   self.pos.y + v_offset - TILE * index)

    def do_not_render(self):
        surface = pg.Surface((TILE * 5, TILE * 7), pg.SRCALPHA)
        surface.fill((40, 40, 0))
        return surface
