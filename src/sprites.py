import pygame
from src.common import *
from src.spritesheet import *
from src.common import *

class Sprites:


	'''class ScoreBoardSprite(pygame.sprite.Sprite):
		def __init__(self, scoreboard: ScoreBoard, WIDTH, HEIGHT, SCALE):
			self.font = pygame.font.Font(None, 32)
			super().__init__()

			self.scoreboard = scoreboard
			self.image = pygame.Surface([WIDTH * SCALE, len(scoreboard.scores) * SCALE])
			self.rect = self.image.get_rect()
			self.SCALE = SCALE

		def update(self):
			self.image.fill("white")
			for i, (player, score) in enumerate(self.scoreboard.scores.items()):
				self.image.blit(
					self.font.render(f"{player}: {score}", True, "green", "white"),
					(0, i * self.SCALE),
				)'''


	class Background(pygame.sprite.Sprite):

		def __init__(self, position):
			self.position = position

		def sprite(self, s_type):
			sprt = Sprites.Background_Sprite()
			self.sprite = sprt.set_sprite(s_type)


	class Background_Sprite(pygame.sprite.Sprite): #tree

		def __init__(self, position):
			self.position = position

		def set_sprite (self, type):
			self.type = type
			self.collision = True #TODO - make a switch case based on type to figure out if collision

		'''def update(self):
			# Render
			self.image.blit(
				self.image,
				(get_scale() * self.position[0], get_scale() * self.position[1]),
			)'''

	#TODO - terrain doesn't have a texture, or at least isn't using it on the current version
	class Terrain(pygame.sprite.Sprite): #treeModel

		def __init__(self, b_sprite, texture):

			self.b_sprite = b_sprite
			self.texture = texture

			self.image = pygame.Surface([SCALE, SCALE])
			#self.image.fill("brown")
			#self.image.blit(self.texture, (0, 0))
			'''self.image.set_colorkey("white")'''

			self.rect = self.image.get_rect()
			self.rect.x = self.b_sprite.position[0] * SCALE
			self.rect.y = self.b_sprite.position[1] * SCALE

		def get_texture(self):
			return self.texture

	#TODO?
	class PC_sprites(pygame.sprite.Sprite):

		def __init__(self):
			pass





if __name__ == "__main__":

	bs = Sprites.Background([0,0])
	#print(bs.position)

	bs.sprite(1)


