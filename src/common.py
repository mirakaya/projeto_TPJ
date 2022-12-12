import pygame
SCALE = 40
WIDTH = 0
HEIGHT = 0

GAME_EVENT = pygame.event.custom_type()

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



