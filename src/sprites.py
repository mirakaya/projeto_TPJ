import pygame
from pygame import transform

from src.common import *
from src.spritesheet import *
from src.scoreboard import *
from src.Playable_character import *
from src.food import *

class ScoreBoardSprite(pygame.sprite.Sprite):
	def __init__(self, scoreboard: ScoreBoard, measures):
		self.font = pygame.font.Font(None, 32)
		super().__init__()
		self.measures = measures
		self.scoreboard = scoreboard
		self.image = pygame.Surface([self.measures.get_width() * self.measures.get_scale(), len(scoreboard.scores) * self.measures.get_scale()])
		self.rect = self.image.get_rect()



	def update(self):
		self.image.fill("white")
		for i, (player, score) in enumerate(self.scoreboard.scores.items()):
			self.image.blit(
				self.font.render(f"{player}: {score}", True, "black", "white"),
				(0, i * self.measures.get_scale()),
			)

class FoodSprite(pygame.sprite.Sprite):

	def __init__(self, food: Food, measures):
		super().__init__()

		FOOD_SPRITESHEET = SpriteSheet("../resources/Sprite sheet.png")
		self.measures = measures
		self.food = food
		CELL_SIZE = 16


		food_image_rect = (0, 7 * CELL_SIZE, CELL_SIZE, CELL_SIZE)
		self.food_image = FOOD_SPRITESHEET.image_at(food_image_rect, -1)
		self.food_image = pygame.transform.scale(self.food_image, (measures.get_scale(), measures.get_scale()))

		self.image = pygame.Surface([measures.get_width() * measures.get_scale(), measures.get_height() * measures.get_scale()])
		self.rect = self.image.get_rect()
		self.update()


	def update(self):
		self.image.fill("white")
		self.image.set_colorkey("white")

		# Render Food
		self.image.blit(
		    self.food_image,
		    (self.measures.get_scale() * self.food.position[0], self.measures.get_scale() * self.food.position[1]),
		)


class Character_Sprite(pygame.sprite.Sprite):
	def __init__(self, character: Playable_character, measures):
		super().__init__()

		CHARACTER_SPRITESHEET = SpriteSheet("../resources/Characters run.png")

		self.character = character
		self.measures = measures
		CELL_SIZE = 16

		character_image_rect = (0, 0, CELL_SIZE, CELL_SIZE)
		self.character_image = CHARACTER_SPRITESHEET.image_at(character_image_rect, -1)
		self.character_image = pygame.transform.scale(self.character_image, (measures.get_scale(), measures.get_scale()))

		self.image = pygame.Surface([measures.get_width() * measures.get_scale(), measures.get_height() * measures.get_scale()])
		self.rect = self.image.get_rect()
		self.update()

	def update(self):
		self.image.fill("white")
		self.image.set_colorkey("white")

		# Render character
		self.image.blit(self.character_image,(self.measures.get_scale() * self.character.pos.x, self.measures.get_scale() * self.character.pos.y), )

'''class Background(pygame.sprite.Sprite):

	def __init__(self, position):
		self.position = position

	def sprite(self, s_type):
		sprt = Background_Sprite()
		self.sprite = sprt.set_sprite(s_type)'''


'''class Background_Sprite(pygame.sprite.Sprite): #tree

	def __init__(self, measures):
		self.measures = measures
		
	def set_sprite (self, type):
		self.type = type
		self.collision = True #TODO - make a switch case based on type to figure out if collision
		
	def update(self):
		# Render
		self.image.blit(
			self.image,
			(get_scale() * self.position[0], get_scale() * self.position[1]),
		)'''

#inherits position from Background_Sprite and has its own texture
'''class Terrain(pygame.sprite.Sprite): #treeModel

	def __init__(self, b_sprite, texture, position):

		self.b_sprite = b_sprite
		self.texture = texture
		self.position = position

		self.image = pygame.Surface([self.measures.get_scale(), self.measures.get_scale()])

		self.rect = self.image.get_rect()
		self.rect.x = self.b_sprite.position[0] * self.measures.get_scale()
		self.rect.y = self.b_sprite.position[1] * self.measures.get_scale()
		
	def get_texture(self):
		return self.texture'''



class TerrainIcon():

	def __init__(self, typeTerrain, measures):
		self.typeTerrain = typeTerrain
		self.measures = measures
		CELL_SIZE = 16

		if typeTerrain == 0: #load floor
			self.image = transform.scale(SpriteSheet("../resources/Textures-16.png").image_at(
				(1 * CELL_SIZE, 0 * CELL_SIZE, CELL_SIZE, CELL_SIZE), -1),
				(self.measures.get_scale(), self.measures.get_scale()),
			)
		elif typeTerrain == 1: #load sky
			self.image = transform.scale(SpriteSheet("../resources/Textures-16.png").image_at(
				(8 * CELL_SIZE, 12 * CELL_SIZE, CELL_SIZE, CELL_SIZE), -1),
				(self.measures.get_scale(), self.measures.get_scale()),
			)

	def get_image(self):
		return self.image

	def get_measures(self):
		return self.measures



class Terrain(pygame.sprite.Sprite):

	def __init__(self, position, t_icon):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.t_icon = t_icon
		self.image = self.t_icon.get_image()

		self.rect = self.t_icon.get_image().get_rect()
		self.rect.x = self.position[0] * self.t_icon.get_measures().get_scale()
		self.rect.y = self.position[1] * self.t_icon.get_measures().get_scale()





#if __name__ == "__main__":

	'''bs = Sprites.Background([0,0])
	#print(bs.position)

	bs.sprite(1)'''

	'''tmp_display = pygame.display.set_mode((0, 0))
	measures = Measures(27, 0, 0, tmp_display)
	icon = TerrainIcon(1, measures )
	Terrain((0,0), icon)'''


