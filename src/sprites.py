import pygame
from pygame import *
from src.spritesheet import *
from src.scoreboard import *
from src.Playable_character import *
from src.food import *
from src.common import *

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

		self.measures.set_character_image_dimensions(self.character_image.get_width(), self.character_image.get_height())

		self.image = pygame.Surface([measures.get_width() * measures.get_scale(), measures.get_height() * measures.get_scale()])
		self.rect = pygame.Rect(self.measures.get_scale() * self.character.pos.x,
			self.measures.get_scale() * self.character.pos.y,
			self.character_image.get_width(),
			self.character_image.get_height())
		self.update()

	def update(self):
		self.image.fill("white")
		self.image.set_colorkey("white")

		# Render character
		self.image.blit(self.character_image,(self.measures.get_scale() * self.character.pos.x - 5,
			self.measures.get_scale() * self.character.pos.y - 5), )
		self.rect.update(self.character.pos.x, self.character.pos.y, self.image.get_width(), self.image.get_height())

		pygame.draw.rect(self.measures.get_display(), (255, 0, 0), pygame.Rect(
			self.measures.get_scale() * self.character.pos.x,
			self.measures.get_scale() * self.character.pos.y,
			self.character_image.get_width(),
			self.character_image.get_height()
		))

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

	def __init__(self, position, t_icon, collision):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.t_icon = t_icon
		self.image = self.t_icon.get_image()
		self.collision = collision

		if self.collision == True:

			self.rect = pygame.Rect(self.position[0] * self.t_icon.get_measures().get_scale(), self.position[1] * self.t_icon.get_measures().get_scale(), self.t_icon.get_image().get_width(),
		                 self.t_icon.get_image().get_height())

			solids.append(self.rect)
			print(self.position[0], self.position[1])

			print(solids)

	'''def update(self):
		self.image.fill("white")
		self.image.set_colorkey("white")

		# Render character
		self.image.blit(self.t_icon.get_image(), (
		self.t_icon.get_measures().get_scale() * self.position[0], self.t_icon.get_measures().get_scale() * self.position[1]), )

		if self.collision == True:
			self.rect = pygame.Rect(self.position[0] * self.t_icon.get_measures().get_scale(), self.position[1] * self.t_icon.get_measures().get_scale(), self.t_icon.get_image().get_width(),
			                 self.t_icon.get_image().get_height())

			pygame.draw.rect(self.t_icon.get_measures().get_display(), (255, 0, 0), pygame.Rect(
				self.position[0] * self.t_icon.get_measures().get_scale(), self.position[1] * self.t_icon.get_measures().get_scale(), self.t_icon.get_image().get_width(),
				self.t_icon.get_image().get_height()
			))

			solids.append(self.rect)

		print(solids)'''

'''		pygame.draw.rect(self.t_icon.get_measures().get_display(), (255,0,0), pygame.Rect(
			self.position[0] * self.t_icon.get_measures().get_scale(),
			self.position[1] * self.t_icon.get_measures().get_scale(),
			self.t_icon.get_image().get_width(),
			self.t_icon.get_image().get_height()))'''




#if __name__ == "__main__":

'''bs = Sprites.Background([0,0])
	#print(bs.position)

	bs.sprite(1)'''

'''tmp_display = pygame.display.set_mode((0, 0))
	measures = Measures(27, 0, 0, tmp_display)
	icon = TerrainIcon(1, measures )
	Terrain((0,0), icon)'''


