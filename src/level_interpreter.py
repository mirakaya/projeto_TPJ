import pygame

from src.common import *
from src.sprites import Terrain


class LevelInterpreter:

	def interpret_level(self, path, measures):
		# reads a .txt file per line and returns its contents
		counter = 0
		lvl_content = ""
		window_title = ""
		width = 0
		height = 0

		is_First_line = True

		with open(path) as content:
			for line in content:

				if counter == 0:
					window_title = line
					#print("wt", window_title)

				elif counter == 1:
					width = int(line)
					#print("wid", width)

				elif counter == 2:
					height = int(line) + 1
					#print("ht", height)

				else:

					if is_First_line == True:
						lvl_content += "I" * width
						is_First_line = False

					lvl_content += line

				counter += 1

		measures.set_height(height)
		measures.set_width(width)

		#create the display with the desired width and height
		display = pygame.display.set_mode((measures.get_scale() * measures.get_width() , measures.get_scale() * measures.get_height()))

		measures.set_display(display)

		#print("lvl", lvl_content)
		return window_title, lvl_content


	def convert_to_terrain(lvl_content, measures, terrains):

		aux_x = 0
		aux_y = 0

		# interpret level into
		for i in lvl_content:
			if i != '\n':
				# convert i to Terrain
				terrain_chosen = terrains[2]
				if i == "F": #floor
					#lvl_map[aux_x][aux_y] = terrains[0]
					platforms.add(Terrain((aux_x, aux_y), terrains[0], True))

				elif i == "S": #sky
					#lvl_map[aux_x][aux_y] = terrains[1]
					background.add(Terrain((aux_x, aux_y), terrains[1], False))

				elif i == "I": #invisible
					background.add(Terrain((aux_x, aux_y), terrains[2], False))

				aux_x += 1
				if aux_x == measures.get_width():
					aux_x = 0
					aux_y += 1



'''if __name__ == "__main__":

	LevelInterpreter().interpret_level('../levels/9.txt')'''


