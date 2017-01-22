import pygame as pg
from pyxit.entity import Entity
from pyxit.player_sprite import PlayerSprite
from .ball import Ball, COLORS


class Objective(Entity):

    def __init__(self, game, ref, pos):
        super(Objective, self).__init__(game, pos.x, pos.y)
        self.ref = ref
        self.set_sprites()

    def set_sprites(self):
        self.sprites = []
        for color in reversed(self.ref.pattern):
            sprite = PlayerSprite(self.game, './assets/frutas.pyxel', 0, 0, sprite_layer='Layer 0')
            self.sprites.append(sprite)
            sprite.change_to(COLORS[color])

    def change_ref(self, new_ref):
        self.ref = new_ref
        self.set_sprites()

    def render(self):
        surface = pg.Surface((16, 16 * len(self.sprites)), pg.SRCALPHA)
        for i, s in enumerate(self.sprites):
            surface.blit(s.render(), (0, 16 * i))
        return surface
