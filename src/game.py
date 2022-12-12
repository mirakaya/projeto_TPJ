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
floor = image.load("../resources/black.jpg")
floor = transform.scale(floor, (SCALE * 10, SCALE * 10))

sky = image.load("../resources/blue.jpg")
sky = transform.scale(sky, (SCALE * 10, SCALE * 10))

bs = Sprites.Background_Sprite(position=[get_width() * get_scale(), get_height() * get_scale()])

terrains = [
	Sprites.Terrain(bs, floor),
	Sprites.Terrain(bs, sky)

	]

# paint background
display.fill("white")

map = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]

aux_x = 0
aux_y = 0

'''print("w - ", WIDTH)
print("h - ", HEIGHT)'''

# interpret level into
for i in lvl_content:
	if i != '\n':
		# convert i to Terrain
		terrain_chosen = terrains[0]
		if i == "F":
			terrain_chosen = terrains[0]

		elif i == "S":
			terrain_chosen = terrains[1]

		map[aux_x][aux_y] = terrain_chosen

		aux_x += 1
		if aux_x == WIDTH:
			aux_x = 0
			aux_y += 1

# render level textures
for x in range(0, len(map) - 1):
	for y in range(0, len(map[0]) - 1):
		display.blit(map[x][y].texture, [x * SCALE, y * SCALE])


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



	# update window + fps
	pygame.display.flip()
	clock.tick(15)


#exit
pygame.quit()