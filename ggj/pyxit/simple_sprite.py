import pygame as pg
from io import BytesIO
from pyxit.entity import Entity


class SimpleSprite(Entity):
    def __init__(self, game, zip, path, x, y):
        super(SimpleSprite, self).__init__(game, x, y)
        self.surface = pg.image.load(BytesIO(zip.read(path)), path)

    def render(self):
        return self.surface
