

class Sniffer(object):

    def __init__(self, model):
        self.model = model

    def get_balls(self):
        """ Returns a dictionary with the balls as keys
        and location as values """
        ret = {}
        s = self.model.scene

        for i, ball in enumerate(s.left_tube.balls):
            if ball is not None:
                ret[ball] = ('left tube', i)

        for i, ball in enumerate(s.right_tube.balls):
            if ball is not None:
                ret[ball] = ('right tube', i)

        for y in range(s.table.y):
            for x in range(s.table.x):
                ball = s.table.matrix[y][x]
                if ball is not None:
                    ret[ball] = ('table', x, y)

        return ret

    def get_ball_from_table(self):
        return self.model.ball_from_table

    def get_ball_from_tube(self):
        return self.model.ball_from_tube

    def get_left_magnet_position(self):
        return self.model.scene.left_magnet.current_pos

    def get_right_magnet_position(self):
        return self.model.scene.right_magnet.current_pos

    def get_objectives(self):
        return list(enumerate(x.pattern for x in self.model.objectives))
