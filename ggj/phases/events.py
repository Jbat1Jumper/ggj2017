from pyxit.game_phase import GamePhase
import pygame as pg


class EventsPhase(GamePhase):

    def __init__(self, game):
        self.game = game
        self.keymap = {
            'a': 'left_left',
            'd': 'right_left',
            'w': 'up_left',
            's': 'down_left',
            'left': 'left_right',
            'right': 'right_right',
            'up': 'up_right',
            'down': 'down_right',
            'p': 'swap_player'
        }

    def keyname(self, key):
        n = pg.key.name(key)
        if n in self.keymap:
            return self.keymap[n]

    def run_phase(self, entities, delta):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game.running = False
            if event.type == pg.KEYDOWN:
                self.process_keypress(event.key)
            if event.type == pg.KEYUP:
                self.process_keyrelease(event.key)

    def process_keypress(self, key):
        self.process_key(key, 'press')

    def process_keyrelease(self, key):
        self.process_key(key, 'release')

    def process_key(self, key, where):
        sm = self.game.state_machine
        s = sm.get_current()
        m = 'on_{}_{}'.format(self.keyname(key), where)
        if hasattr(s, m):
            m = getattr(s, m)
            if callable(m):
                m()
