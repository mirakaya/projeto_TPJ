from src.common import EVENT_INCREASE_SCORE

class ScoreBoard:
    def __init__(self, players):
        self.scores = {}
        for p in players:
            p.register(EVENT_INCREASE_SCORE, self.score)
            self.scores[p.name] = p.my_score

    def score(self, context):
        self.scores[context.name] += 1000