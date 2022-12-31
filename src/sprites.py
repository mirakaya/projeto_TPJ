import pygame
from pygame import *
from src.spritesheet import *
from src.scoreboard import *
from src.Playable_character import *
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
				(0, i * self.measures.get_scale() / 2),
			)


class Character_Sprite(pygame.sprite.Sprite):

	def __init__(self, character: Playable_character, measures, type):
		super().__init__()

		CHARACTER_SPRITESHEET = SpriteSheet("../resources/01-generic.png")

		self.character = character
		self.measures = measures
		self.type = type

		CELL_SIZE = 16

		character_image_rect = (0, 0, CELL_SIZE, CELL_SIZE)
		self.character_image = CHARACTER_SPRITESHEET.image_at(character_image_rect, -1)
		self.character_image = pygame.transform.scale(self.character_image, (measures.get_scale(), measures.get_scale())).convert()

		self.measures.set_character_image_dimensions(self.character_image.get_width(), self.character_image.get_height())

		self.image = pygame.Surface([measures.get_width() * measures.get_scale(), measures.get_height() * measures.get_scale()])
		self.rect = pygame.Rect(self.measures.get_scale() * self.character.pos.x,
			self.measures.get_scale() * self.character.pos.y,
			self.character_image.get_width(),
			self.character_image.get_height())

		self.character.character_dimensions.x = self.character_image.get_width()
		self.character.character_dimensions.y = self.character_image.get_height()

		self.update()

	def update(self):

		self.image.fill("white")
		self.image.set_colorkey("white")

		#if jumping, continue jump
		if self.character.jumping == True:
			self.character.jump()
		else: #else, check if feet are hitting the ground, if not, jump at max
			is_collision = self.character.vertical_collision(solids)
			if is_collision == 0:
				self.character.jump_count = self.character.max_jump_val
				self.character.jumping = True
			'''else:
				self.character.jumping = False
				self.character.jump_count = 0
'''


		#check if character is collecting a heart
		collected = self.character.check_collision(collectibles)
		if collected != None:
			self.character.score += 1000
			self.character.notify(EVENT_INCREASE_SCORE)
			collectibles.remove(collected)

			for i in hearts:
				if i.rect == collected:
					i.kill()


		# Render character
		self.character.measures.get_display().blit(self.character_image, [self.measures.get_scale() * self.character.pos.x, self.measures.get_scale() * self.character.pos.y])

		self.rect = pygame.Rect(self.measures.get_scale() * self.character.pos.x,
		                        self.measures.get_scale() * self.character.pos.y,
		                        self.character_image.get_width(),
		                        self.character_image.get_height())

		# check if character reached the end
		if self.character.check_collision(end) != None:
			self.character.score += 1000
			self.character.notify(EVENT_INCREASE_SCORE)
			pygame.event.post(EVENT_END_LEVEL)
			print("end")


class TerrainIcon():

	def __init__(self, typeTerrain, measures):
		self.typeTerrain = typeTerrain
		self.measures = measures
		CELL_SIZE = 16

		if typeTerrain == 0: #load floor
			self.image = transform.scale(SpriteSheet("../resources/Textures-16.jpg").image_at(
				(15 * CELL_SIZE, 4 * CELL_SIZE, CELL_SIZE, CELL_SIZE), -1),
				(self.measures.get_scale(), self.measures.get_scale()),
			).convert_alpha()

		elif typeTerrain == 1: #load sky
			self.image = transform.scale(SpriteSheet("../resources/Textures-16.png").image_at(
				(8 * CELL_SIZE, 12 * CELL_SIZE, CELL_SIZE, CELL_SIZE), -1),
				(self.measures.get_scale(), self.measures.get_scale()),
			).convert_alpha()

		elif typeTerrain == 2: #load invisible
			self.image = transform.scale(SpriteSheet("../resources/Textures-16.jpg").image_at(
				(30 * CELL_SIZE, 0 * CELL_SIZE, CELL_SIZE, CELL_SIZE), -1),
				(self.measures.get_scale(), self.measures.get_scale()),
			).convert_alpha()

		elif typeTerrain == 3: #load finish
			self.image = transform.scale(SpriteSheet("../resources/Textures-16.jpg").image_at(
				(0 * CELL_SIZE, 31 * CELL_SIZE, CELL_SIZE, CELL_SIZE), -1),
				(self.measures.get_scale(), self.measures.get_scale()),
			).convert_alpha()

		elif typeTerrain == 4: #load heart
			self.image = transform.scale(pygame.image.load("../resources/heart.png"),
				(self.measures.get_scale(), self.measures.get_scale()),
			).convert_alpha()

	def get_image(self):
		return self.image

	def get_measures(self):
		return self.measures

	def get_type(self):
		return self.typeTerrain



class Terrain(pygame.sprite.Sprite):

	def __init__(self, position, t_icon, collision):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.t_icon = t_icon
		self.image = self.t_icon.get_image()
		self.collision = collision

		self.rect = pygame.Rect(self.position[0] * self.t_icon.get_measures().get_scale(), self.position[1] * self.t_icon.get_measures().get_scale(), self.t_icon.get_image().get_width(), self.t_icon.get_image().get_height())

		if self.t_icon.get_type() == 0:
			solids.append(self.rect)
		elif self.t_icon.get_type() == 3:
			end.append(self.rect)
		elif self.t_icon.get_type() == 4:
			collectibles.append(self.rect)


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


