import pygame
from pygame import *

class Scoreboard:

	def render_scoreboard(self, text, display_surface, width, height):

		font = pygame.font.SysFont(None, 15)
		img = font.render(str(text), True, (0,0,0))
		display_surface.blit(img, (width, height))





