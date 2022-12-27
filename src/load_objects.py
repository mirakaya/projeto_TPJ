from pygame import *
from src.sprites import Background_Sprite, Terrain


def load_terrain(measures):


	floor = image.load("../resources/floor.png")
	floor = transform.scale(floor, (measures.get_scale(), measures.get_scale()))

	sky = image.load("../resources/sky.png")
	sky = transform.scale(sky, (measures.get_scale(), measures.get_scale()))

	bs = Background_Sprite(
		position=[measures.get_width() * measures.get_scale(), measures.get_height() * measures.get_scale()])

	terrains = [
		Terrain(bs, floor, measures),
		Terrain(bs, sky, measures)

	]

	return terrains