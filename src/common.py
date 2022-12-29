import pygame
from enum import Enum
from datetime import datetime


class Directions(Enum):
	UP = (0, -1)
	DOWN = (0, 1)
	LEFT = (-1, 0)
	RIGHT = (1, 0)


GAME_EVENT = pygame.event.custom_type()

EVENT_FOOD_EATEN = "event_food_eaten"

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()  # collision
background = pygame.sprite.Group()  # no collision
character = pygame.sprite.Group()


'''class CSAccess():

	def __init__(self):
		self.char_sprite = None

	def set_char_sprite(self, cs):
		self.char_sprite = cs

	def get_char_sprite(self):
		return self.char_sprite'''


'''def set_scale (new_val):
	SCALE = new_val'''


# -----------

class Measures():

	def __init__(self, scale, width, height, display):
		self.scale = scale
		self.width = width
		self.height = height
		self.display = display

	def get_scale(self):
		return self.scale

	def set_height(self, new_height):
		self.height = new_height

	def get_height(self):
		return self.height

	def set_width(self, new_width):
		self.width = new_width

	def get_width(self):
		return self.width

	def set_display(self, display):
		self.display = display

	def get_display(self):
		return self.display


# -----------

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


def remove_values_from_list(lst, val):
	return [value for value in lst if value != val]
