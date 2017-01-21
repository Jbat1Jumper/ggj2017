
import random

DEFAULT_PATTERN_SIZE = 3


class Objective(object):

    def __init__(self, model):
        self.model = model

    def check_conditions(self):
        """
        This method return wheter the defined objective is completed.
        Must be overwritten in subclass
        """
        return False


class PatternObjective(Objective):

    def __init__(self, model, pattern=None):
        super(PatternObjective, self).__init__(model)

        self.pattern = pattern or self.get_random_pattern()

    def get_random_pattern(self, size=DEFAULT_PATTERN_SIZE):
        m = self.model.scene.table.matrix
        return random.sample([x.color for row in m for x in row], size)

    def check_conditions(self):
        balls = [x.color for x in self.model.tube.balls if x]
        n = len(self.pattern)
        return any((self.pattern == balls[i:i+n]) for i in range(len(balls) - n + 1))

    def __str__(self):
        return str(list(reversed(self.pattern)))
