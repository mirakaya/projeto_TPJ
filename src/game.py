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

#set clock
clock = pygame.time.Clock()

#get all files in the levels dir
lvl_dir = '../levels/'
entries = os.listdir(lvl_dir)
current_level = 0

#load first level
LevelInterpreter.load_level(lvl_dir + entries[0])

#initialize objects
mc = Playable_character()
scoreboard = ScoreBoard(mc)

#group of all non level texture sprites - mc, scoreboard, other items
all_sprites = pygame.sprite.Group()
all_sprites.add(ScoreBoardSprite(scoreboard, WIDTH, HEIGHT, SCALE))
#TODO - add mc



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
	all_sprites.draw(get_display())



	# update window + fps
	pygame.display.flip()
	clock.tick(15)


#exit
pygame.quit()