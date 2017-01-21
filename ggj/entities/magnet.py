from pyxit.entity import Entity
import pygame as pg

TILE = 16


class Magnet(Entity):

    def __init__(self, game, pos, is_left=False):
        super(Magnet, self).__init__(game, pos.x, pos.y)
        self.is_left = is_left

    def render(self):
        surface = pg.Surface((16, 16), pg.SRCALPHA)
        surface.fill((230, 0, 0))
        return surface
