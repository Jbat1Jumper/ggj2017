
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

    def check_conditions(self, tube):
        balls = [x.color for x in tube.balls if x]
        n = len(self.pattern)
        return self.pattern == balls[:n]

    def __str__(self):
        return str(list(reversed(self.pattern)))


class PatternObjectivesGenerator(object):

    def __init__(self, model, number, length):
        self.model, self.number, self.length = model, number, length

        self.objectives = []
        total_size = number * length
        self.m = self.model.scene.table.matrix
        pattern = random.sample([x.color for row in self.m for x in row], total_size)

        for i in range(0, total_size, length):
            objective = PatternObjective(model, pattern[i:min(i + length, total_size)])
            self.objectives.append(objective)

    def replace_objective(self, objective):
        self.objectives.remove(objective)
        balls = [x.color for row in self.m for x in row]
        for color in [x for obj in self.objectives for x in obj.pattern]:
            try:
                balls.remove(color)
            except ValueError:
                pass
        new_obj = PatternObjective(self.model, random.sample(balls, self.length))
        self.objectives.append(new_obj)
