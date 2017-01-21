

class Vec(object):

    def __init__(self, x=None, y=None):
        self.x = float(x) or 0.0
        self.y = float(y) or 0.0


class Entity(object):
    def __init__(self, x, y):
        self.pos = Vec(x, y)


class PhysicalEntity(Entity):
    def __init__(self, x, y, w, h):
        super(PhysicalEntity, self).__init__(x, y)
        self.w = w
        self.h = h
        self.x_speed = 0
        self.y_speed = 0
        self.static = True

    def collide(self, other):
        assert(isinstance(other, PhysicalEntity))
        s, o = self, other
        if s.pos.x + s.w > o.pos.x \
                and o.pos.x + o.w > s.pos.x \
                and s.pos.y + s.h > o.pos.y \
                and o.pos.y + o.h > s.pos.y:
            return True
        return False


class Tile(PhysicalEntity):
    pass
