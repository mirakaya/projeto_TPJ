import pygame
SCALE = 40
WIDTH = 0
HEIGHT = 0

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