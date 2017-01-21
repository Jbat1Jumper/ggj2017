import pygame as pg
from io import BytesIO
from zipfile import ZipFile
from json import loads
from pyxit.entity import PhysicalEntity


class PlayerSprite(PhysicalEntity):

    def __init__(self, game, path, x, y):
        super(PlayerSprite, self).__init__(game, x, y, 1, 1)  # (1, 1) is temporary
        self.static = False
        self.sprite_layer = self.sprite_layer if hasattr(self, 'sprite_layer') else 'Sprite'
        self.animations = {}
        self.current_animation = None
        self.current_milliseconds = 0
        self.flipped = False
        self._read_spritesheet(path)

    def _read_spritesheet(self, path):
        with ZipFile(path) as zip:
            data = loads(zip.open('docData.json').read().decode('utf-8'))

            layer_file, layer_data = self._get_sprite_layer(zip, data)
            layer_surface = pg.image.load(BytesIO(zip.read(layer_file)),
                                          layer_file)

            tile_width = data['canvas']['tileWidth']
            tile_height = data['canvas']['tileHeight']

            self.w = tile_width
            self.h = tile_height

            # canvas_height = data['canvas']['height']
            canvas_width = data['canvas']['width']
            for index, anim in data['animations'].items():
                n_anim = {
                    'frames': [],
                    'durations': [],
                    'length': 0,
                    'duration': 0
                }
                for n in range(anim['length']):
                    surface = pg.Surface((tile_width, tile_height), pg.SRCALPHA)

                    hpos = ((anim['baseTile'] + n) * tile_width)
                    xo = hpos % canvas_width
                    yo = hpos / canvas_width * tile_height
                    surface.blit(layer_surface,
                                 (0, 0),
                                 (xo, yo, tile_width, tile_height))

                    n_anim['length'] += 1
                    n_anim['frames'].append(surface)
                    frame_duration = anim['frameDurationMultipliers'][n] \
                        * anim['frameDuration'] / 100.0
                    n_anim['durations'].append(frame_duration)
                    n_anim['duration'] += frame_duration

                self.animations[anim['name']] = n_anim
                if self.current_animation is None:
                    self.current_animation = anim['name']

    def _get_sprite_layer(self, zip, data):
        for index, layer in data['canvas']['layers'].items():
            if layer['name'] == self.sprite_layer:
                return 'layer{}.png'.format(index), layer
        raise Exception('theres no "{}" layer in {}'.format(self.sprite_layer, zip))

    def render(self):
        c = 0
        current_animation = self.animations[self.current_animation]
        current_animation_len = len(current_animation['frames'])
        for frame_number in range(current_animation_len):
            c += current_animation['durations'][frame_number]
            if c > (self.current_milliseconds % current_animation['duration']):
                frame = current_animation['frames'][frame_number]
                if self.flipped:
                    frame = pg.transform.flip(frame, True, False)
                return frame
        raise Exception('theres no frame to render?')

    def advance(self, milliseconds):
        self.current_milliseconds += milliseconds

    def change_to(self, animation_name, milliseconds=None):
        if milliseconds is not None:
            self.current_milliseconds = milliseconds
        if animation_name == self.current_animation:
            return
        if animation_name not in self.animations:
            raise Exception('no such animation {}'.format(animation_name))
        self.current_animation = animation_name

    def flip(self, flipped=None):
        if flipped is not None:
            self.flipped = flipped
        else:
            self.flipped = not self.flipped
