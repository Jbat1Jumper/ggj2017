from pyxit.entity import Entity


class Ball(Entity):

    def __init__(self, game, ref, pos):
        super(Ball, self).__init__(game, pos.x, pos.y)
        self.ref = ref
