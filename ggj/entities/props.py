from pyxit.simple_sprite import SimpleSprite
from pyxit.player_sprite import PlayerSprite
from zipfile import ZipFile


def prepare_props(game):
    game.props = {}


def create_background(game):
    zip = ZipFile('assets/fondo.pyxel')

    bg1 = SimpleSprite(game, zip, 'layer2.png', 0, 0)
    bg0 = SimpleSprite(game, zip, 'layer1.png', 0, 0)

    game.create_entity(bg1)
    game.create_entity(bg0)

    game.props['bg1'] = bg1
    game.props['bg0'] = bg0


def create_foregraund(game):
    zip = ZipFile('assets/fondo.pyxel')

    fg0 = SimpleSprite(game, zip, 'layer0.png', 0, 0)

    game.create_entity(fg0)

    game.props['fg0'] = fg0


def create_nahuelito(game):
    n = PlayerSprite(game, 'assets/cabeza nahuelito.pyxel', 16 * 4, 16 * 10,
                     sprite_layer='Layer 0')
    game.create_entity(n)
    game.props['n_izq_cabeza'] = n

    n = PlayerSprite(game, 'assets/cuerpo nahuelito.pyxel', 16, 16 * 7,
                     sprite_layer='Layer 0')
    game.create_entity(n)
    game.props['n_izq_cuerpo'] = n

    n = PlayerSprite(game, 'assets/culo de nahuelito.pyxel', 16, 16 * 6,
                     sprite_layer='Layer 0')
    game.create_entity(n)
    game.props['n_izq_culo'] = n

    n = PlayerSprite(game, 'assets/cabeza nahuelito.pyxel', 16 * 15, 16 * 10,
                     sprite_layer='Layer 0')
    n.flip()
    game.create_entity(n)
    game.props['n_der_cabeza'] = n

    n = PlayerSprite(game, 'assets/cuerpo nahuelito.pyxel', 16 * 17, 16 * 7,
                     sprite_layer='Layer 0')
    n.flip()
    game.create_entity(n)
    game.props['n_der_cuerpo'] = n

    n = PlayerSprite(game, 'assets/culo de nahuelito.pyxel', 16 * 17, 16 * 6,
                     sprite_layer='Layer 0')
    n.flip()
    game.create_entity(n)
    game.props['n_der_culo'] = n
