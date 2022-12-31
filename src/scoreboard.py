from src.common import EVENT_FOOD_EATEN


class ScoreBoard:
    def __init__(self, players):
        self.scores = {}

        for p in players:

            p.register(EVENT_FOOD_EATEN, self.score)
            self.scores[p.name] = p.score

            print(self.scores[p.name], p.name)

    def score(self, context):
        self.scores[context.name] += 1000






'''import pygame
from pygame import *
from src.sprites import *

class Scoreboard:

	def render_scoreboard(self, text, display_surface, width, height):

		font = pygame.font.SysFont(None, 30)
		img = font.render(str(text), True, (0,0,0))
		display_surface.blit(img, (width, height))

		#self.render(display_surface, width, height)'''





'''	def render(self, display_surface, width, height):# draw snake - render

		bs = Sprites.Background_Sprite(position=[width * get_scale(), height * get_scale()])
		texture = image.load("../resources/black.jpg")
		texture = transform.scale(texture, (SCALE*10, SCALE*10))


		terrain = Sprites.Terrain(bs, texture)

		display_surface.blit(terrain, (width * get_scale(), height * get_scale()))'''










