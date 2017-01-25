

class GamePhase(object):
    name = 'Empty Phase'

    def entity_created(self, entity):
        pass

    def entity_deleted(self, entity):
        pass

    def run_phase(self, entities, delta):
        pass
