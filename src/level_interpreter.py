import pygame

from src import common
from src.common import *

class LevelInterpreter:

	def interpret_level(self, path, measures):
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

		measures.set_height(height)
		measures.set_width(width)

		#create the display with the desired width and height
		display = pygame.display.set_mode((measures.get_scale() * measures.get_width() , measures.get_scale() * measures.get_height()))

		measures.set_display(display)



		print(measures.get_height())
		print(measures.get_width())

		#print("lvl", lvl_content)
		return window_title, lvl_content

	def render_level(lvl_map, measures):
		# render level textures
		for x in range(0, len(lvl_map)):
			for y in range(0, len(lvl_map[0])):
				measures.get_display().blit(lvl_map[x][y].texture, [x * measures.get_scale(), y * measures.get_scale()])


'''if __name__ == "__main__":

	LevelInterpreter().interpret_level('../levels/1.txt')'''


