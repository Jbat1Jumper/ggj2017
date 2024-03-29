import pygame as pg


class Game(object):

    def __init__(self):
        self.phases = []
        self.entities = []
        self.clock = None
        self.clock_fps = 20.0
        self.time = 0.0
        self.running = False
        self.screen = None
        self.screen_size = (12 * 32, 10 * 32)

    def add_phase(self, phase):
        self.phases.append(phase)

    def create_entity(self, entity):
        if entity in self.entities:
            return
        self.entities.append(entity)
        for phase in self.phases:
            phase.entity_created(entity)

    def load(self):
        pass

    def run(self):
        self.start()
        self.load()
        self.running = True
        while self.running:
            delta = self.clock.tick(self.clock_fps)
            for phase in self.phases:
                    phase.run_phase(self.entities, delta)
            self.time += delta
        self.quit()

    def start(self):
        pg.init()
        pg.display.set_caption('Pygame + Pyxel Edit (Test 2)')
        pg.display.set_mode(self.screen_size)
        self.clock = pg.time.Clock()
        self.screen = pg.display.get_surface()

    def quit(self):
        print('GAME OVER')
        pg.quit()
        quit()
