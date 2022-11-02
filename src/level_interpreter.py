import pygame

SCALE = 10

class LevelInterpreter:

	def interpret_level(self, path):
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
		display = pygame.display.set_mode((SCALE * width, SCALE * height))

		#print("lvl", lvl_content)
		return window_title, width, height, lvl_content, display


'''if __name__ == "__main__":

	LevelInterpreter().interpret_level('../levels/1.txt')'''


