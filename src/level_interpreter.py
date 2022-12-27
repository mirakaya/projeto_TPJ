from pygame import *
from src.sprites import *
from src.Playable_character import *


class LevelInterpreter:

	def interpret_lvl_file(self, path):
		# reads a .txt file per line and returns its contents
		counter = 0
		lvl_content = ""
		window_title = ""
		width = 0
		height = 0

		with open(path) as content:
			for line in content:

				if counter == 0:
					window_title = line
					#print("wt", window_title)

				elif counter == 1:
					width = int(line)
					#print("wid", width)

				elif counter == 2:
					height = int(line)
					#print("ht", height)

				else:
					lvl_content += line

				counter += 1


		#create the display with the desired width and height
		display = pygame.display.set_mode((get_scale() * width, get_scale() * height))
		set_display(display)

		#print("lvl", lvl_content)
		return window_title, width, height, lvl_content,

	def load_level(file_path):

		window_title, WIDTH, HEIGHT, lvl_content = LevelInterpreter().interpret_lvl_file(file_path)

		#save the values on common
		set_width(WIDTH)
		set_height(HEIGHT)


		#load floor image
		floor = image.load("../resources/floor.png")
		floor = transform.scale(floor, (get_scale(), get_scale()))

		#load sky image
		sky = image.load("../resources/sky.png")
		sky = transform.scale(sky, (get_scale(), get_scale()))

		bs = Background_Sprite(position=[get_width() * get_scale(), get_height() * get_scale()])

		terrains = [
			Terrain(bs, floor),
			Terrain(bs, sky)

		]

		# paint background
		get_display().fill("white")

		map = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
		aux_x = 0
		aux_y = 0

		# interpret level into
		for i in lvl_content:
			if i != '\n':
				# convert i to Terrain
				terrain_chosen = terrains[0]
				if i == "F":
					map[aux_x][aux_y] = terrains[0]

				elif i == "S":
					map[aux_x][aux_y] = terrains[1]

				aux_x += 1
				if aux_x == WIDTH:
					aux_x = 0
					aux_y += 1

		LevelInterpreter.render_level(map)

	def render_level(lvl_map):

		# render level textures
		for x in range(0, len(lvl_map)):
			for y in range(0, len(lvl_map[0])):
				get_display().blit(lvl_map[x][y].texture, [x * get_scale(), y * get_scale()])



'''if __name__ == "__main__":

	LevelInterpreter().interpret_level('../levels/1.txt')'''


