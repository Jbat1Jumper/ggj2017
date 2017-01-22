from pyxit.simple_sprite import SimpleSprite
from zipfile import ZipFile


class Background():

    def __init__(self, game):
        zip = ZipFile('assets/fondo.pyxel')
        layer2 = SimpleSprite(game, zip, 'layer2.png', 0, 0)
        layer1 = SimpleSprite(game, zip, 'layer1.png', 0, 0)

        game.create_entity(layer2)
        game.create_entity(layer1)


class Foreground():

    def __init__(self, game):
        zip = ZipFile('assets/fondo.pyxel')
        layer0 = SimpleSprite(game, zip, 'layer0.png', 0, 0)

        game.create_entity(layer0)
