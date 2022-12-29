import pygame
import os
from src.level_interpreter import LevelInterpreter
from src.sprites import *
from src.Playable_character import *
from src.load_objects import *
from src.food import *


running = True
list_keys = []
pygame.init()

#set clock
clock = pygame.time.Clock()

#initialize measures
tmp_display = pygame.display.set_mode((0,0))
measures = Measures(27, 0, 0, tmp_display)

#get all files in the levels dir
lvl_dir = '../levels/'
entries = os.listdir(lvl_dir)


for level in entries:

	#load level content from file
	window_title, lvl_content = LevelInterpreter().interpret_level(lvl_dir + level, measures)

	#loads terrain TODO - see if it fits better in another class, probs whatever class has the terrains
	terrains = load_terrain(measures)

	#convert the content to terrains
	lvl_map, platforms = LevelInterpreter.convert_to_terrain(lvl_content, measures, terrains)

	#render the level
	LevelInterpreter.render_level(lvl_map, measures)

	#initialize objects
	mc = Playable_character(measures, "Alex",(5,5))
	mc.controls(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)
	scoreboard = ScoreBoard(mc)
	food = Food((0,0))

	#group of all non level texture sprites - mc, scoreboard, other items
	all_sprites = pygame.sprite.Group()
	all_sprites.add(ScoreBoardSprite(scoreboard, measures))
	all_sprites.add(Character_Sprite(mc, measures))
	all_sprites.add(FoodSprite(food, measures))
	all_sprites.add(platforms)

	while running: #game

		#event handler
		for event in pygame.event.get():

			if event.type == pygame.QUIT: #quit game TODO - get way to finish game and finish level, probs not the same
				running = False

			elif event.type == pygame.KEYDOWN : #a key is pressed
				list_keys.append(event.key)

			elif event.type == pygame.KEYUP : #a key is relased
				list_keys = remove_values_from_list(list_keys, key)

			'''if cmd:
				command_log.append(cmd)'''

			'''elif event.type == GAME_EVENT:
				if event.name == EVENT_FOOD_EATEN:
					pass'''

		if len(list_keys) != 0 : #execute key commands
			for key in list_keys:
				cmd = mc.command(key)


		# render the level
		LevelInterpreter.render_level(lvl_map, measures)
		#update sprites
		all_sprites.update()
		all_sprites.draw(measures.get_display())

		# update window + fps
		pygame.display.flip()
		clock.tick(15)


#exit
pygame.quit()