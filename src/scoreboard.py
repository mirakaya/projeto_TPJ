from src.common import EVENT_FOOD_EATEN


class ScoreBoard:
    def __init__(self, *players):
        self.scores = {}
        for p in players:
            p.register(EVENT_FOOD_EATEN, self.score)
            self.scores[p.name] = 0

    def score(self, context):
        self.scores[context.name] += 1
