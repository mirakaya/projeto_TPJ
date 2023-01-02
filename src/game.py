import pygame
import os
from src.level_interpreter import LevelInterpreter
from src.sprites import *
from src.Playable_character import *

running = True
list_keys = []
pygame.init()

#set clock
clock = pygame.time.Clock()

#get all files in the levels dir
lvl_dir = '../levels/'
entries = os.listdir(lvl_dir)

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 30)

score1 = 0
score2 = 0

scale = 30

tmp_x = 30 * 30
tmp_y = 30 * 15

# initialize measures
tmp_display = pygame.display.set_mode((tmp_x, tmp_y))
pygame.display.set_caption("Speed & Gather")
measures = Measures(1, 0, 0, tmp_display)

#start screen
measures.get_display().fill("gray")

font_t = pygame.font.Font(None, 80)
text_t = font_t.render('Speed & Gather', True, "black")
textRect = text_t.get_rect()
textRect.center = (tmp_x // 2, tmp_y // 2 - 40)
measures.get_display().blit(text_t, textRect)

font_s = pygame.font.Font(None, 40)
text_s = font_s.render('Press any key to start', True, "black")
textRect = text_s.get_rect()
textRect.center = (tmp_x // 2, tmp_y // 2 + 40)
measures.get_display().blit(text_s, textRect)

pygame.display.flip()

no_start = True
while no_start:
	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:  # a key is pressed
			no_start = False


#game
for level in entries:

	#load level content from file
	window_title, lvl_content = LevelInterpreter().interpret_level(lvl_dir + level, measures, scale)

	# loads terrain
	terrains = [TerrainIcon(0, measures), TerrainIcon(1, measures), TerrainIcon(2, measures), TerrainIcon(3, measures), TerrainIcon(4, measures)]

	#convert the content to terrain groups
	character_coordinates = LevelInterpreter.convert_to_terrain(lvl_content, measures, terrains)

	#initialize objects
	mc = Playable_character(measures, score1, "Player 1", character_coordinates)
	mc.controls(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)

	mc2 = Playable_character(measures, score2, "Player 2", character_coordinates)
	mc2.controls(pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT)

	scoreboard = ScoreBoard([mc, mc2])

	#group of all non level texture sprites - scoreboard, background, platforms and hearts
	all_sprites.add(background)
	all_sprites.add(ScoreBoardSprite(scoreboard, measures))
	all_sprites.add(platforms)
	all_sprites.add(hearts)

	#group with character
	character.add(Character_Sprite(mc, measures, 1))
	character.add(Character_Sprite(mc2, measures, 2))

	game_incomplete = True

	while running and game_incomplete: #game

		#event handler
		for event in pygame.event.get():

			if pygame.key.get_pressed()[K_ESCAPE]:
				print("esc")
				game_incomplete = False

			if event.type == pygame.QUIT: #quit game
				running = False

			elif event.type == pygame.KEYDOWN : #a key is pressed
				list_keys.append(event.key)


			elif event.type == pygame.KEYUP : #a key is relased
				list_keys = remove_values_from_list(list_keys, key)


			if event == EVENT_END_LEVEL :
				game_incomplete = False

			'''if cmd:
				command_log.append(cmd)'''

			'''elif event.type == GAME_EVENT:
				if event.name == EVENT_FOOD_EATEN:
					pass'''

		if len(list_keys) != 0 : #execute key commands
			for key in list_keys:
				cmd = mc.command(key)
				cmd = mc2.command(key)


		# render the level
		measures.get_display().fill("gray")
		all_sprites.update()
		all_sprites.draw(measures.get_display())

		if game_incomplete == True:
			character.update()
			character.draw(measures.get_display())

		# update window + fps
		pygame.display.flip()
		clock.tick(15)

		#print("FPS:", int(clock.get_fps()))

	#clean up
	all_sprites.empty()
	platforms.empty()
	character.empty()
	background.empty()
	hearts.empty()

	solids.clear()
	end.clear()
	collectibles.clear()

	#save scores for next level
	score1 = mc.score
	score2 = mc2.score


#end screen
measures.get_display().fill("gray")

font_t = pygame.font.Font(None, 80)
text_t = font_t.render('Scores', True, "black")
textRect = text_t.get_rect()
textRect.center = (tmp_x // 2, tmp_y // 2 - 40)
measures.get_display().blit(text_t, textRect)

font_s = pygame.font.Font(None, 40)
text_s = font_s.render(mc.name + " : " + str(mc.score), True, "black")
text_s2 = font_s.render(mc2.name + " : " + str(mc2.score), True, "black")
textRect_s = text_s.get_rect()
textRect_s2 = text_s2.get_rect()
textRect_s.center = (tmp_x // 2, tmp_y // 2 + 50)
textRect_s2.center = (tmp_x // 2, tmp_y // 2 + 100)
measures.get_display().blit(text_s, textRect_s)
measures.get_display().blit(text_s2, textRect_s2)

pygame.display.set_caption("Speed & Gather")
pygame.display.flip()

no_end = True
while no_end:
	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:  # a key is pressed
			no_end = False

#exit
pygame.quit()