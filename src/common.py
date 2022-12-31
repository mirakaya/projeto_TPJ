import pygame
from enum import Enum

class Directions(Enum):
	UP = (0, -1)
	DOWN = (0, 1)
	LEFT = (-1, 0)
	RIGHT = (1, 0)


GAME_EVENT = pygame.event.custom_type()

EVENT_INCREASE_SCORE = "event_increase_score"
EVENT_END_LEVEL = pygame.event.Event(pygame.USEREVENT, attr1='EVENT_END_LEVEL')


all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()  # collision
background = pygame.sprite.Group()  # no collision
character = pygame.sprite.Group()
hearts = pygame.sprite.Group()

solids = []
end = []
collectibles = []


class Measures():

	def __init__(self, scale, width, height, display, character_image_dimensions=(0,0)):
		self.scale = scale
		self.width = width
		self.height = height
		self.display = display
		self.character_image_dimensions = character_image_dimensions

	def set_scale(self, new_scale):
		self.scale = new_scale

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

	def set_character_image_dimensions(self, width, height):
		self.character_image_dimensions = (width, height)

	def get_character_image_dimensions(self):
		return self.character_image_dimensions


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
