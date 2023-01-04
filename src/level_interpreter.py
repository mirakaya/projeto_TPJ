from src.common import *
from src.sprites import Terrain

class LevelInterpreter:

	def interpret_level(self, path, measures, scale): # reads a .txt file per line and returns its contents

		counter = 0
		lvl_content = ""
		window_title = ""
		width = 0
		height = 0

		is_First_line = True

		with open(path) as content: #read file and interpret
			for line in content:

				if counter == 0:
					window_title = line

				elif counter == 1:
					width = int(line)

				elif counter == 2:
					height = int(line) + 1

				else:

					if is_First_line == True:
						lvl_content += "I" * width
						is_First_line = False

					lvl_content += line

				counter += 1

		measures.set_height(height)
		measures.set_width(width)
		measures.set_scale(scale)

		#create the display with the desired width and height
		display = pygame.display.set_mode((measures.get_scale() * measures.get_width() , measures.get_scale() * measures.get_height()) )
		pygame.display.set_caption(window_title)
		measures.set_display(display)

		return window_title, lvl_content


	def convert_to_terrain(lvl_content, measures, terrains):

		aux_x = 0
		aux_y = 0

		character_coordinates = (0,0)

		# interpret level into
		for i in lvl_content:
			if i != '\n':

				# convert i to Terrain
				if i == "F": #floor
					platforms.add(Terrain((aux_x, aux_y), terrains[0]))

				elif i == "S": #sky
					background.add(Terrain((aux_x, aux_y), terrains[1]))

				elif i == "I": #invisible
					background.add(Terrain((aux_x, aux_y), terrains[2]))

				elif i == "E": #finish
					background.add(Terrain((aux_x, aux_y), terrains[1]))
					background.add(Terrain((aux_x, aux_y), terrains[3]))

				elif i == "H": #heart
					background.add(Terrain((aux_x, aux_y), terrains[1]))
					hearts.add(Terrain((aux_x, aux_y), terrains[4]))

				elif i == "P": #spikes
					background.add(Terrain((aux_x, aux_y), terrains[5]))

				elif i == "C": #character
					background.add(Terrain((aux_x, aux_y), terrains[1]))
					character_coordinates = (aux_x, aux_y - 1)

				aux_x += 1
				if aux_x == measures.get_width():
					aux_x = 0
					aux_y += 1

		return character_coordinates
