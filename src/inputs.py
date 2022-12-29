import pygame

from src.common import Directions


class Command:
    def execute(self):
        raise NotImplemented
    def fast_forward(self):
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


class Dash(Command):
    def execute(self, actor):
        self.actor = actor
        actor.dash()


class InputHandler:
    command = {
        pygame.K_w: Up(),
        pygame.K_a: Left(),
        pygame.K_s: Down(),
        pygame.K_d: Right(),
        pygame.K_e: Dash(),

    }

    def handleInput(self, key):
        try:
            print(self.command[key])
            return self.command[key]

        except KeyError:
            print("Key not bound - ignore input")