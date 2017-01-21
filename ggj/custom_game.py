
from pyxit.game import Game
from pyxit.game_phase import GamePhase
from pyxit.tile_map import TileMap
from pyxit.entity import PhysicalEntity


class CustomGame(Game):

    def __init__(self):
        super(CustomGame, self).__init__()

    def load(self):
        self.add_phase(CustomPhase(self))


class CustomPhase(GamePhase):

    def __init__(self, game):
        self.game = game

    def run_phase(self, entities, delta):
        print 'I\'m custom phase and i\'m running!'
