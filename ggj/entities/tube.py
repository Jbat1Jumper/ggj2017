from pyxit.entity import Entity
from pyxit.vec import Vec


class Tube(Entity):

    @classmethod
    def left_one(cls, game):
        t = cls(game, 16, 80)
        t.is_left = True
        t.body_h_offset = 16
        return t

    @classmethod
    def right_one(cls, game):
        t = cls(game, 240, 80)
        t.is_left = False
        t.body_h_offset = 16 * 3
        return t

    def position_for(self, index):
        v_offset = 16 * 6
        return Vec(self.pos.x + self.body_h_offset,
                   self.pos.y + v_offset - 16 * index)
