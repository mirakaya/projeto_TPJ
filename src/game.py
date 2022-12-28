import pygame
import os
from src.inputs import InputHandler
from src.level_interpreter import LevelInterpreter
from src.scoreboard import *
from src.common import *
from pygame import *
from src.sprites import *
from src.Playable_character import *
from src.load_objects import *
from src.food import *


running = True
pygame.init()

#set clock
clock = pygame.time.Clock()

#initialize measures
tmp_display = pygame.display.set_mode((0,0))
measures = Measures(40, 0, 0, tmp_display)

#get all files in the levels dir
lvl_dir = '../levels/'
entries = os.listdir(lvl_dir)


for level in entries:

	#load level content from file
	window_title, lvl_content = LevelInterpreter().interpret_level(lvl_dir + level, measures)

	#loads terrain TODO - see if it fits better in another class, probs whatever class has the terrains
	terrains = load_terrain(measures)

	# paint background
	measures.get_display().fill(181425)

	#convert the content to terrains
	lvl_map = LevelInterpreter.convert_to_terrain(lvl_content, measures, terrains)

	#render the level
	LevelInterpreter.render_level(lvl_map, measures)

	#initialize objects
	mc = Playable_character()
	scoreboard = ScoreBoard(mc)
	food = Food([100,100])


	#group of all non level texture sprites - mc, scoreboard, other items
	all_sprites = pygame.sprite.Group()
	all_sprites.add(ScoreBoardSprite(scoreboard, measures))
	all_sprites.add(Character_Sprite(mc, measures))
	all_sprites.add(FoodSprite(food, measures))



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
		all_sprites.draw(measures.get_display())

		# update window + fps
		pygame.display.flip()
		clock.tick(15)


#exit
pygame.quit()