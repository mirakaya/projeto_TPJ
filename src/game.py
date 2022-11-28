import pygame
import os
from src.inputs import InputHandler
from src.level_interpreter import LevelInterpreter
from src.scoreboard import Scoreboard
from src.common import *
from pygame import *
from src.sprites import *

running = True
pygame.init()

#get all files in the levels dir
lvl_dir = '../levels/'
entries = os.listdir(lvl_dir)
current_level = 0

window_title, WIDTH, HEIGHT, lvl_content, display = LevelInterpreter().interpret_level(lvl_dir + entries[current_level])

set_width(WIDTH)
set_height(HEIGHT)


#initialize display
#WIDTH, HEIGHT = 80, 40
'''SCALE = 10
display = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))'''

#clock
clock = pygame.time.Clock()

#TODO - tmp
texture = image.load("../resources/sugar.jpg")
texture = transform.scale(texture, (SCALE * 10, SCALE * 10))

terrains = [
	Sprites.Terrain(texture),

	]


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

	map = [[0 for x in range(get_width())] for y in range(get_height())]

	x = 0
	y = 0

	#interpret level into
	for i in lvl_content:
		if i != '\n':
			#TODO - tmp
			map [x][y] = i
			#Scoreboard().render_scoreboard(i, display, x * get_scale(), y * get_scale())
			x += 1
			if x == WIDTH:
				x = 0
				y += 1

	#render level

	for x in map:
		for y in map:
			render_position(x, y)


	# update window + fps
	pygame.display.flip()
	clock.tick(15)


#exit
pygame.quit()