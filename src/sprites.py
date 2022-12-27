import pygame
from src.common import *
from src.spritesheet import *
from src.scoreboard import *
from src.Playable_character import *

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

class CharacterSprite(pygame.sprite.Sprite):
	def __init__(self, character: Playable_character, measures):
		super().__init__()

		character_sprite = SpriteSheet("../resources/Characters run.png")
		CELL_SIZE = 16
		self.character = character


		character_map = {
			("walk", Directions.UP): (0, 0),
			("walk", Directions.RIGHT): (0, 1),
			("walk", Directions.LEFT): (1, 0),
			("walk", Directions.DOWN): (1, 1),

		}

		# Load and resize images to SCALE
		self.character_images = {
			name: pygame.transform.scale(
				character_sprite.image_at(
					(a * CELL_SIZE, b * CELL_SIZE, CELL_SIZE, CELL_SIZE), -1
				),
				(measures.get_scale(), measures.get_scale()),
			)
			for (name, (a, b)) in character_map.items()
		}

		self.image = pygame.Surface([measures.get_width() * measures.get_scale(), measures.get_height() * measures.get_scale()])
		self.update()
		self.rect = self.image.get_rect()

	def update(self):
		self.image.fill("white")
		self.image.set_colorkey("white")

		# Render character

		'''def get_direction(x, y, prev_x, prev_y):
			"""given 2 coordinates returns direction taken."""
			dir = None
			if x - prev_x > 0:
				dir = Directions.RIGHT
			elif x - prev_x < 0:
				dir = Directions.LEFT
			elif y - prev_y > 0:
				dir = Directions.DOWN
			elif y - prev_y < 0:
				dir = Directions.UP
			return dir

		# Get Head
		prev_x, prev_y = self.character.body[0]
		prev_dir = None

		# Walk from 1st body position towards tail
		for x, y in self.character.body[1:]:

			dir = get_direction(x, y, prev_x, prev_y)
			if prev_dir is None:
				image = ("head", self.character.direction)
			else:
				image = (prev_dir, dir)

			# blit previous body part now that we now directions taken
			self.image.blit(
				self.character_images[image], (self.SCALE * prev_x, self.SCALE * prev_y)
			)

			prev_x, prev_y = x, y
			prev_dir = dir

		# Finally blit tail
		self.image.blit(
			self.character_images[("tail", prev_dir)],
			(self.SCALE * prev_x, self.SCALE * prev_y),
		)'''


class Background(pygame.sprite.Sprite):

	def __init__(self, position):
		self.position = position

	def sprite(self, s_type):
		sprt = Background_Sprite()
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

	def __init__(self, b_sprite, texture, measures):

		self.b_sprite = b_sprite
		self.texture = texture

		self.image = pygame.Surface([measures.get_scale(), measures.get_scale()])
		#self.image.fill("brown")
		#self.image.blit(self.texture, (0, 0))
		'''self.image.set_colorkey("white")'''

		self.rect = self.image.get_rect()
		self.rect.x = self.b_sprite.position[0] * measures.get_scale()
		self.rect.y = self.b_sprite.position[1] * measures.get_scale()

	def get_texture(self):
		return self.texture







'''if __name__ == "__main__":

	bs = Sprites.Background([0,0])
	#print(bs.position)

	bs.sprite(1)'''


