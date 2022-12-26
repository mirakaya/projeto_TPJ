import pygame
from src.common import *
from src.spritesheet import *
from src.scoreboard import *
from src.Playable_character import *

class Sprites:


	class ScoreBoardSprite(pygame.sprite.Sprite):
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
				)

	class CharacterSprite(pygame.sprite.Sprite):
		def __init__(self, character: Playable_character, WIDTH, HEIGHT, SCALE):
			super().__init__()

			SNAKE_SPRITESHEET = SpriteSheet("tea.png")

			self.character = character
			self.SCALE = SCALE

			'''snake_map = {
				("head", Directions.UP): (3, 0),
				("head", Directions.RIGHT): (4, 0),
				("head", Directions.LEFT): (3, 1),
				("head", Directions.DOWN): (4, 1),
				(Directions.UP, Directions.RIGHT): (0, 0),
				(Directions.LEFT, Directions.DOWN): (0, 0),
				(Directions.DOWN, Directions.RIGHT): (0, 1),
				(Directions.LEFT, Directions.UP): (0, 1),
				(Directions.LEFT, Directions.LEFT): (1, 0),
				(Directions.RIGHT, Directions.RIGHT): (1, 0),
				(Directions.RIGHT, Directions.DOWN): (2, 0),
				(Directions.UP, Directions.LEFT): (2, 0),
				(Directions.UP, Directions.UP): (2, 1),
				(Directions.DOWN, Directions.DOWN): (2, 1),
				(Directions.RIGHT, Directions.UP): (2, 2),
				(Directions.DOWN, Directions.LEFT): (2, 2),
				("tail", Directions.UP): (4, 3),
				("tail", Directions.DOWN): (3, 2),
				("tail", Directions.RIGHT): (3, 3),
				("tail", Directions.LEFT): (4, 2),
			}

			# Load and resize images to SCALE
			self.snake_images = {
				name: pygame.transform.scale(
					SNAKE_SPRITESHEET.image_at(
						(a * CELL_SIZE, b * CELL_SIZE, CELL_SIZE, CELL_SIZE), -1
					),
					(SCALE, SCALE),
				)
				for (name, (a, b)) in snake_map.items()
			}

			self.image = pygame.Surface([WIDTH * SCALE, HEIGHT * SCALE])
			self.update()
			self.rect = self.image.get_rect()'''

		def update(self):
			self.image.fill("white")
			self.image.set_colorkey("white")

			# Render snake

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
			prev_x, prev_y = self.snake.body[0]
			prev_dir = None

			# Walk from 1st body position towards tail
			for x, y in self.snake.body[1:]:

				dir = get_direction(x, y, prev_x, prev_y)
				if prev_dir is None:
					image = ("head", self.snake.direction)
				else:
					image = (prev_dir, dir)

				# blit previous body part now that we now directions taken
				self.image.blit(
					self.snake_images[image], (self.SCALE * prev_x, self.SCALE * prev_y)
				)

				prev_x, prev_y = x, y
				prev_dir = dir

			# Finally blit tail
			self.image.blit(
				self.snake_images[("tail", prev_dir)],
				(self.SCALE * prev_x, self.SCALE * prev_y),
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


