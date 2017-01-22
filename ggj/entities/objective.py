import pygame as pg
from pyxit.entity import Entity
from pyxit.player_sprite import PlayerSprite
from .ball import Ball, COLORS


class Objective(Entity):

    def __init__(self, game, colors, pos):
        super(Objective, self).__init__(game, pos.x, pos.y)
        self.colors = colors

        self.sprites = []
        for c in colors:
            sprite = PlayerSprite(game, './assets/frutas.pyxel', 0, 0, sprite_layer='Layer 0')
            self.sprites.append(sprite)
            sprite.change_to(COLORS[c])

    def render(self):
        surface = pg.Surface((16 * len(self.sprites), 16), pg.SRCALPHA)
        for i, s in enumerate(self.sprites):
            surface.blit(s.render(), (16 * i, 0))
        return surface
