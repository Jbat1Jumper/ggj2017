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

    def move(self, pos):
        a = self.game.animation

        start = self.pos
        end = pos

        def foo(progress):
            self.pos.x = start.x * (1 - progress) + end.x * progress
            self.pos.y = start.y * (1 - progress) + end.y * progress

        a.create(500, foo)
