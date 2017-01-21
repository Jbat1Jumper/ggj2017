import pygame as pg
from cStringIO import StringIO
from pyxit.entity import Entity


class SimpleSprite(Entity):
    def __init__(self, zip, path, x, y):
        super(SimpleSprite, self).__init__(x, y)
        self.surface = pg.image.load(StringIO(zip.read(path)), path)

    def render(self):
        return self.surface
