from enum import Enum
from src.common import *
from src.fsm_characters import *
from src.inputs import Up, Down, Left, Right


class Playable_character(Actor, Subject):

	def __init__(self, measures, score,  name=None, init_pos=(0, 0)):
		Subject.__init__(self)
		self.name = name
		self.dead = 0
		self.control_keys = dict()
		self.measures = measures

		self.pos = pygame.math.Vector2(init_pos)
		self.vel = pygame.math.Vector2(0, 0)
		self.velocity_value = 0.5

		self.jumping = False
		self.jump_count = 0
		self.max_jump_val = 8

		self.character_dimensions = pygame.math.Vector2(0, 0)

		self.rectified = False

		self.register(EVENT_INCREASE_SCORE, self.increase_score)
		self.my_score = score

	def increase_score(self, context):
		self.my_score += 1000

	def controls(self, up, left, down, right):
		self.control_keys = {up: Up, left: Left, down: Down, right: Right}

	def command(self, control):
		if control in self.control_keys.keys():
			cmd = self.control_keys[control]()
			cmd.execute(self)
			return cmd

	def move(self, direction: Directions):

		if direction == Directions.LEFT:
			self.vel.x = -self.velocity_value

		if direction == Directions.RIGHT:
			self.vel.x = self.velocity_value

		if self.horizontal_collision(solids) == False:
			self.pos.x += self.vel.x
			self.rectified = False

	def jump(self):

		self.jumping = True

		if self.jump_count < self.max_jump_val:
			self.vel.y = -self.velocity_value

		else: #falling
			self.vel.y = self.velocity_value

		if self.vertical_collision(solids) == 0:
			self.pos.y += self.vel.y

		self.jump_count += 1


	def cancel_jump(self):
		self.jump_count = self.max_jump_val

	def stop(self):
		self.vel.x = 0
		self.vel.y = 0

	def horizontal_collision(self, object_list):

		aux_rect = pygame.Rect(self.measures.get_scale() * self.pos.x + 2 * self.vel.x,
		                       self.measures.get_scale() * self.pos.y + 2 * self.vel.y,
		                       self.character_dimensions.x,
		                       self.character_dimensions.y)

		for i in object_list:
			if pygame.Rect.colliderect(aux_rect, i) :
				return True

		return False

	def vertical_collision(self, object_list): #0 no collision, 1 hitting feet, 2 hitting head

		aux_rect = pygame.Rect(self.measures.get_scale() * self.pos.x + 2 * self.vel.x,
		                       self.measures.get_scale() * self.pos.y + 2 * self.vel.y,
		                       self.character_dimensions.x,
		                       self.character_dimensions.y)

		for i in object_list:
			if pygame.Rect.colliderect(aux_rect, i) :

				if self.pos.y == i.top / self.measures.get_scale() - 1:
					#hitting feet
					self.jumping = False
					self.jump_count = 0
					self.stop()
					return 1

				else:
					#hitting head
					self.jump_count = self.max_jump_val
					self.stop()
					return 2

		return 0

	def check_collision(self, object_list):

		aux_rect = pygame.Rect(self.measures.get_scale() * self.pos.x + 2 * self.vel.x,
		                       self.measures.get_scale() * self.pos.y + 2 * self.vel.y,
		                       self.character_dimensions.x,
		                       self.character_dimensions.y)

		for i in object_list:
			if pygame.Rect.colliderect(aux_rect, i):
				return i

		return None

	def set_position(self, position):
		self.pos = position

