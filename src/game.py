import pygame
import os
from src.inputs import InputHandler
from src.level_interpreter import LevelInterpreter
from src.scoreboard import Scoreboard


running = True
pygame.init()

#get all files in the levels dir
lvl_dir = '../levels/'
entries = os.listdir(lvl_dir)
current_level = 0

window_title, WIDTH, HEIGHT, lvl_content, display = LevelInterpreter().interpret_level(lvl_dir + entries[current_level])

#initialize display
#WIDTH, HEIGHT = 80, 40
'''SCALE = 10
display = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))'''

#clock
clock = pygame.time.Clock()


while running: #game

	#event handler
	for event in pygame.event.get():

		if event.type == pygame.QUIT: #quit game
			running = False

		elif event.type == pygame.KEYDOWN: #a key is pressed

			command = InputHandler().handleInput(event.key) #go get the right input
			#command.execute(snake1) #and execute it with obj snake1

		#elif event.type == GAME_EVENT:
		#	print(event.txt)

	#paint background
	display.fill("white")

	x = 0
	y = 0
	scale = 10
	# temp code
	for i in lvl_content:
		if i != '\n':
			Scoreboard().render_scoreboard(i, display, x * scale, y * scale)
			x +=1
			if x == WIDTH:
				x=0
				y+= 1


	# update window + fps
	pygame.display.flip()
	clock.tick(15)


#exit
pygame.quit()