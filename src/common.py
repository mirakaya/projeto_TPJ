import pygame
from enum import Enum

#events
GAME_EVENT = pygame.event.custom_type()
EVENT_INCREASE_SCORE = "event_increase_score"
EVENT_END_LEVEL = pygame.event.Event(pygame.USEREVENT, attr1='EVENT_END_LEVEL')

def write_to_screen(text, size_font, x, y, displacement, measures):
	font_t = pygame.font.Font(None, size_font)
	text_t = font_t.render(text, True, "black")
	textRect = text_t.get_rect()
	textRect.center = (x // 2, y // 2 - displacement)
	measures.get_display().blit(text_t, textRect)


#directions
class Directions(Enum):
	UP = (0, -1)
	DOWN = (0, 1)
	LEFT = (-1, 0)
	RIGHT = (1, 0)

#groups of sprites
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()  # collision
background = pygame.sprite.Group()  # no collision
character = pygame.sprite.Group()
hearts = pygame.sprite.Group()

#group of rect of the objects with collision
solids = []
end = []
collectibles = []
spikes = []

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
