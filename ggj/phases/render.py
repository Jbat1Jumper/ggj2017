from pyxit.game_phase import GamePhase
import pygame as pg


class RenderPhase(GamePhase):

    def __init__(self, game, screen, size):
        self.game = game
        self.screen = screen
        self.size = size
        self.surface = pg.Surface(size, pg.SRCALPHA)
        self.bg_color = (240, 240, 250)

    def run_phase(self, entities, delta):
        self.surface.fill(self.bg_color)
        for entity in entities:
            self.animate(entity, delta)
            self.blit_entity(entity)
        self.screen.blit(pg.transform.scale(self.surface,
                                            self.screen.get_size()),
                         (0, 0))
        pg.display.update()

    def animate(self, entity, delta):
        if hasattr(entity, 'animate'):
            entity.animate(delta)

    def blit_entity(self, entity):
        if hasattr(entity, 'render'):
            self.surface.blit(entity.render(), (entity.pos.x, entity.pos.y))
