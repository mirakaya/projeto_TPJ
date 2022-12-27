from pygame import *
from src.sprites import Background_Sprite, Terrain
from src.spritesheet import SpriteSheet


def load_terrain(measures):
	# Load and resize images to SCALE
	'''self.character_images = {
		name: pygame.transform.scale(
			character_sprite.image_at(
				(a * CELL_SIZE, b * CELL_SIZE, CELL_SIZE, CELL_SIZE), -1
			),
			(measures.get_scale(), measures.get_scale()),
		)
		for (name, (a, b)) in character_map.items()
	}'''
	CELL_SIZE = 16
	floor = transform.scale(SpriteSheet("../resources/Textures-16.png").image_at(
			(1 * CELL_SIZE,0 * CELL_SIZE, CELL_SIZE, CELL_SIZE), -1),
			(measures.get_scale(), measures.get_scale()),
		)

	sky = transform.scale(SpriteSheet("../resources/Textures-16.png").image_at(
			(8 * CELL_SIZE,12 * CELL_SIZE, CELL_SIZE, CELL_SIZE), -1),
			(measures.get_scale(), measures.get_scale()),
		)

	bs = Background_Sprite(
		position=[measures.get_width() * measures.get_scale(), measures.get_height() * measures.get_scale()])

	terrains = [
		Terrain(bs, floor, measures),
		Terrain(bs, sky, measures)

	]

	return terrains