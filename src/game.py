import pygame
import os
from src.inputs import InputHandler
from src.level_interpreter import LevelInterpreter
from src.scoreboard import *
from src.common import *
from pygame import *
from src.sprites import *
from src.Playable_character import *


running = True
pygame.init()

#clock
clock = pygame.time.Clock()


#TODO - refactor this to another class or smt
#get all files in the levels dir
lvl_dir = '../levels/'
entries = os.listdir(lvl_dir)
current_level = 0

window_title, WIDTH, HEIGHT, lvl_content, display = LevelInterpreter().interpret_level(lvl_dir + entries[current_level])

set_width(WIDTH)
set_height(HEIGHT)

floor = image.load("../resources/floor.png")
floor = transform.scale(floor, (get_scale(), get_scale()))

sky = image.load("../resources/sky.png")
sky = transform.scale(sky, (get_scale(), get_scale()))

bs = Background_Sprite(position=[get_width() * get_scale(), get_height() * get_scale()])

terrains = [
	Terrain(bs, floor),
	Terrain(bs, sky)

	]

# paint background
display.fill("white")

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

# render level textures
for x in range(0, len(map)):
	for y in range(0, len(map[0])):
		display.blit(map[x][y].texture, [x * get_scale(), y * get_scale()])


#initialize mc
mc = Playable_character()
scoreboard = ScoreBoard(mc)




#group of all non level texture sprites - mc, scoreboard, other items
all_sprites = pygame.sprite.Group()


all_sprites.add(ScoreBoardSprite(scoreboard, WIDTH, HEIGHT, SCALE))

#all_sprites.add(scoreboard)
#all_sprites.add(mc)



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

	#update sprites
	all_sprites.update()
	all_sprites.draw(display)



	# update window + fps
	pygame.display.flip()
	clock.tick(15)


#exit
pygame.quit()