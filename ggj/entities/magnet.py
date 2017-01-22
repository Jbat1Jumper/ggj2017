from pyxit.player_sprite import PlayerSprite
import pygame as pg

TILE = 16


class Magnet(PlayerSprite):

    def __init__(self, game, pos, is_left=False):
        super(Magnet, self).__init__(game, 'assets/red_gnome.pyxel', pos.x, pos.y, 'Layer 0')
        self.is_left = is_left
        if not is_left:
            self.flip()
        self.change_to('redgnome_idle')

    def do_not_render(self):
        surface = pg.Surface((16, 16), pg.SRCALPHA)
        surface.fill((230, 0, 0))
        return surface

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
