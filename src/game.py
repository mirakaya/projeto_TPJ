import pygame
import os
from src.level_interpreter import LevelInterpreter
from src.sprites import *
from src.Playable_character import *
from src.food import *


running = True
list_keys = []
pygame.init()

#set clock
clock = pygame.time.Clock()

#initialize measures
tmp_display = pygame.display.set_mode((0,0))
measures = Measures(1, 0, 0, tmp_display)

#get all files in the levels dir
lvl_dir = '../levels/'
entries = os.listdir(lvl_dir)


for level in entries:

	#load level content from file
	window_title, lvl_content = LevelInterpreter().interpret_level(lvl_dir + level, measures)

	#loads terrain
	terrains = [TerrainIcon(0, measures), TerrainIcon(1, measures), TerrainIcon(2, measures)]

	#convert the content to terrain groups
	LevelInterpreter.convert_to_terrain(lvl_content, measures, terrains)

	#initialize objects
	mc = Playable_character(measures, "Alex",(5,5))
	mc.controls(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)
	scoreboard = ScoreBoard(mc)
	food = Food((0,0))
	character.add(Character_Sprite(mc, measures))


	#group of all non level texture sprites - mc, scoreboard, background, other items
	all_sprites.add(background)
	all_sprites.add(ScoreBoardSprite(scoreboard, measures))


	#all_sprites.add(FoodSprite(food, measures))
	all_sprites.add(platforms)
	#all_sprites.add(character)


	game_incomplete = True
	while running and game_incomplete: #game

		#event handler
		for event in pygame.event.get():

			if event.type == pygame.QUIT: #quit game
				running = False

			elif event.type == pygame.KEYDOWN : #a key is pressed
				list_keys.append(event.key)


			elif event.type == pygame.KEYUP : #a key is relased
				list_keys = remove_values_from_list(list_keys, key)

			#TODO - implement event game finished to change game_incomplete to false

			'''if cmd:
				command_log.append(cmd)'''

			'''elif event.type == GAME_EVENT:
				if event.name == EVENT_FOOD_EATEN:
					pass'''

		if len(list_keys) != 0 : #execute key commands
			for key in list_keys:
				cmd = mc.command(key)


		# render the level
		measures.get_display().fill(181425)
		all_sprites.update()
		all_sprites.draw(measures.get_display())
		'''platforms.update()
		platforms.draw(measures.get_display())'''
		character.update()
		character.draw(measures.get_display())

		# update window + fps
		pygame.display.flip()
		clock.tick(30)

		print("FPS:", int(clock.get_fps()))


#exit
pygame.quit()