from src.common import Directions

class Command:
    def execute(self):
        raise NotImplemented


class Up(Command):
    def execute(self, actor):
        self.actor = actor
        actor.jump()


class Down(Command):
    def execute(self, actor):
        self.actor = actor
        actor.cancel_jump()


class Left(Command):
    def execute(self, actor):
        self.actor = actor
        actor.move(Directions.LEFT)


class Right(Command):
    def execute(self, actor):
        self.actor = actor
        actor.move(Directions.RIGHT)
