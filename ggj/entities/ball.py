from pyxit.player_sprite import PlayerSprite
import pygame as pg

COLORS = {
    1: 'berry_rosa',
    2: 'berry_naranja',
    3: 'berry_verde',
    4: 'berry_amarilla',
    5: 'berry_azul',
}


class Ball(PlayerSprite):

    def __init__(self, game, ref, pos):
        super(Ball, self).__init__(game, './assets/frutas.pyxel', pos.x, pos.y, sprite_layer='Layer 0')
        self.ref = ref
        animation = COLORS[self.ref.color]
        self.change_to(animation)

    def animate(self, delta):
        self.advance(delta)
