from zipfile import ZipFile
from json import loads
import operator
from pyxit.simple_sprite import SimpleSprite
from pyxit.entity import Tile


class TileMap(object):

    def __init__(self, path):
        self.path = path
        self.loaders = {
            'p_': PropsLoader(),
            'e_': EntityLoader(),
            'b_': BackgroundLoader(),
            's_': SolidsLoader(),
            'n_': None
        }

    def add_entity_handler(self, id, callback):
        self.loaders['e_'].add_handler(id, callback)

    def load(self):
        with ZipFile(self.path) as zip:
            data = loads(zip.open('docData.json').read().decode('utf-8'))

            entities = []
            sorted_layers = sorted(data['canvas']['layers'].items(),
                                   key=operator.itemgetter(1))
            for index, layer in sorted_layers:
                layer['index'] = index
                loader = self.loader_for(layer['name'])
                loader.load(layer, entities, data, zip)

            return entities

    def loader_for(self, name):
        prefix = name[:2]
        if prefix in self.loaders.keys():
            return self.loaders[prefix]


class LayerLoader(object):
    def load(self, layer, entities, data, zip):
        pass


class EntityLoader(LayerLoader):
    def __init__(self):
        self.handlers = {}

    def add_handler(self, id, callback):
        self.handlers[id] = callback

    def load(self, layer, entities, data, zip):
        tw = data['canvas']['tileWidth']
        th = data['canvas']['tileHeight']
        w = data['canvas']['width']
        for key, value in layer['tileRefs'].items():
            mod = w / tw
            x = (int(key) % mod) * tw
            y = (int(key) / mod) * th
            id = value['index']
            if id in self.handlers:
                entities.append(self.handlers[id](x, y))


class SolidsLoader(LayerLoader):

    def load(self, layer, entities, data, zip):
        tw = data['canvas']['tileWidth']
        th = data['canvas']['tileHeight']
        w = data['canvas']['width']
        for key, value in layer['tileRefs'].items():
            mod = w / tw
            x = (int(key) % mod) * tw
            y = (int(key) / mod) * th
            entities.append(Tile(x, y, tw, th))


class BackgroundLoader(LayerLoader):
    def load(self, layer, entities, data, zip):
        entities.append(SimpleSprite(zip, 'layer' + layer['index'] + '.png',
                        0, 0))


class PropsLoader(LayerLoader):
    def load(self, layer, entities, data, zip):
        raise NotImplemented()
