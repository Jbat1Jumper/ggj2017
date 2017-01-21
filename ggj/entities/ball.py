from pyxit.entity import Entity
import pygame as pg


class Ball(Entity):

    def __init__(self, game, ref, pos):
        super(Ball, self).__init__(game, pos.x, pos.y)
        self.ref = ref

    def render(self):
        surface = pg.Surface((16, 16), pg.SRCALPHA)
        color = {
            1: (255, 0, 0),
            2: (0, 255, 0),
            3: (0, 0, 255),
            4: (235, 0, 235),
            5: (235, 235, 0)
        }[self.ref.color]
        pg.draw.ellipse(surface, color, (0, 0, 16, 16))
        return surface
