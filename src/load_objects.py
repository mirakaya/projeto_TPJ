'''from pygame import *
from src.sprites import Background_Sprite, Terrain
from src.spritesheet import SpriteSheet'''


'''def load_terrain(measures):

	CELL_SIZE = 16
	floor = transform.scale(SpriteSheet("../resources/Textures-16.png").image_at(
			(1 * CELL_SIZE,0 * CELL_SIZE, CELL_SIZE, CELL_SIZE), -1),
			(measures.get_scale(), measures.get_scale()),
		)

	sky = transform.scale(SpriteSheet("../resources/Textures-16.png").image_at(
			(8 * CELL_SIZE,12 * CELL_SIZE, CELL_SIZE, CELL_SIZE), -1),
			(measures.get_scale(), measures.get_scale()),
		)

	bs = Background_Sprite(measures)

	terrains = [
		Terrain(bs, floor, position),
		Terrain(bs, sky, position= )

	]

	return terrains'''