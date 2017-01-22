import pygame as pg
from pyxit.entity import Entity
from pyxit.player_sprite import PlayerSprite


class ScoreBar(Entity):

    def __init__(self, game, is_left, pos):
        super(ScoreBar, self).__init__(game, pos.x, pos.y)
        self.is_left = is_left
        self.length = 4
        self.score = 0
        self.animations_per_tile = 3

        self.sprites = []
        for i in range(self.length):
            sprite = PlayerSprite(self.game, './assets/barra.pyxel', 0, 0)
            if i == 0:
                sprite.change_to('inicio', milliseconds=0)
            elif i == self.length - 1:
                sprite.change_to('fin', milliseconds=0)
            else:
                sprite.change_to('medio')
            self.sprites.append(sprite)

    def set_score(self, score, max_score):
        self.perc = score / float(max_score)
        total_positions = self.length * self.animations_per_tile
        filled_positions = int(total_positions * self.perc)
        print('setting score')
        print('score', score, max_score)
        print('perc', self.perc)
        print('total_positions', total_positions)
        print('filled_positions', filled_positions)
        for i, sprite in enumerate(self.sprites):
            if filled_positions <= 0:
                break
            a = min(filled_positions, self.animations_per_tile)
            sprite.change_to(milliseconds=100*a-100)
            filled_positions -= self.animations_per_tile

    def render(self):
        surface = pg.Surface((16 * len(self.sprites), 16), pg.SRCALPHA)
        for i, s in enumerate(self.sprites):
            surface.blit(s.render(), (16 * i, 0))
        return surface
