from pyxit.player_sprite import PlayerSprite
import pygame as pg


class Ball(PlayerSprite):

    def __init__(self, game, ref, pos):
        self.sprite_layer = 'Layer 0'
        super(Ball, self).__init__(game, './assets/frutas.pyxel', pos.x, pos.y)
        self.ref = ref
        animation = {
            1: 'berry_rosa',
            2: 'berry_naranja',
            3: 'berry_verde',
            4: 'berry_amarilla',
            5: 'berry_azul',
        }[self.ref.color]
        self.change_to(animation)

    def animate(self, delta):
        self.advance(delta)
