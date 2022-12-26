import pygame
from enum import Enum


SCALE = 40
WIDTH = 0
HEIGHT = 0
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
