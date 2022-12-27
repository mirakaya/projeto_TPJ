import pygame
from enum import Enum
from datetime import datetime

SCALE = 40
WIDTH = 0
HEIGHT = 0
DISPLAY = pygame.display.set_mode((20,20))

class Directions(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

GAME_EVENT = pygame.event.custom_type()

EVENT_FOOD_EATEN = "event_food_eaten"

'''def set_scale (new_val):
	SCALE = new_val'''



def get_scale():
	return SCALE

def set_height (new_val):
	HEIGHT = new_val

def get_height():
	return HEIGHT

def set_width (new_val):
	WIDTH = new_val

def get_width():
	return WIDTH

def set_display(display):
	DISPLAY = display

def get_display():
	return DISPLAY


#--------------------------------

#TODO - actor probs needs changes
class Actor:
    def __init__(self):
        self.name = "Unknown"

    def move(self, direction: Directions):
        raise NotImplemented


class Subject:
    def __init__(self):
        self.events = {}

    def register(self, event, event_handler):
        if event not in self.events:
            self.events[event] = []
        self.events[event].append(event_handler)

    def notify(self, event):
        for event_handler in self.events[event]:
            event_handler(self)

        ev = pygame.event.Event(GAME_EVENT, {'name': event, 'obj': self})
        pygame.event.post(ev)

class Command:
    def __init__(self):
        self.actor = None
        self.dt = datetime.now()

    def execute(self, actor):
        raise NotImplemented

    def __str__(self):
        return f"[{self.dt}] {self.actor.name}: {self.__class__.__name__}"


#TODO - change commands
class Up(Command):
    def execute(self, actor):
        self.actor = actor
        actor.move(Directions.UP)


class Down(Command):
    def execute(self, actor):
        self.actor = actor
        actor.move(Directions.DOWN)


class Left(Command):
    def execute(self, actor):
        self.actor = actor
        actor.move(Directions.LEFT)


class Right(Command):
    def execute(self, actor):
        self.actor = actor
        actor.move(Directions.RIGHT)
