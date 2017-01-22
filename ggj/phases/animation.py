from pyxit.game_phase import GamePhase


class AnimationPhase(GamePhase):

    def __init__(self, game):
        self.game = game
        self.animations = []

    def run_phase(self, entities, delta):
        to_del = []
        for a in self.animations:
            a.update(delta)
            if a.ended:
                to_del.append(a)
        for a in to_del:
            self.animations.remove(a)
            if a.next:
                self.animations.append(a.next)
            a.die()

    def create(self, time, function, callback=None):
        a = Animation(time, function, callback)
        self.animations.append(a)
        return a


class Animation():
    def __init__(self, time, function, callback=None):
        self.current_ms = 0.0
        self.end_ms = time
        self.function = function
        self.callback = callback
        self.ended = False
        self.next = None

    def update(self, delta):
        if self.current_ms >= self.end_ms:
            self.ended = True
            self.current_ms = self.end_ms

        if self.function:
            self.function(float(self.current_ms) / self.end_ms)

        self.current_ms += delta

    def die(self):
        if self.callback:
            self.callback()

    def chain(self, time, function, callback=None):
        self.next = Animation(time, function, callback)
        return self.next
