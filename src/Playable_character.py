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
		self.score = score

		self.pos = pygame.math.Vector2(init_pos)
		self.vel = pygame.math.Vector2(0, 0)
		self.velocity_value = 0.5

		self.jumping = False
		self.jump_count = 0
		self.max_jump_val = 8

		self.character_dimensions = pygame.math.Vector2(0, 0)




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

		#print(self.new_horizontal_collision(solids))
		if self.horizontal_collision(solids) == False:
			self.pos.x += self.vel.x

	def print_vel_x(self):
		print(self.vel.x)


	def jump(self):

		self.jumping = True

		if self.jump_count < self.max_jump_val:
			self.vel.y = -self.velocity_value

		else: #falling
			self.vel.y = self.velocity_value

		#print(self.new_vertical_collision(solids))
		if self.vertical_collision(solids) == 0:
			self.pos.y += self.vel.y

		self.jump_count += 1


	def cancel_jump(self):
		self.vel.y = 2 * self.velocity_value
		self.pos.y += self.vel.y


	def dash(self):
		self.vel.x = 4 * self.vel.x
		self.vel.y = 4 * self.vel.y
		self.pos += self.vel

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
				#self.stop()
				return True

		return False

	def vertical_collision(self, object_list):

		aux_rect = pygame.Rect(self.measures.get_scale() * self.pos.x + 2 * self.vel.x,
		                       self.measures.get_scale() * self.pos.y + 2 * self.vel.y,
		                       self.character_dimensions.x,
		                       self.character_dimensions.y)

		for i in object_list:
			if pygame.Rect.colliderect(aux_rect, i) :

				if self.pos.y == i.top / self.measures.get_scale() - 1:
					#hitting feet
					#print("hitting feet\n\n")
					self.jumping = False
					self.jump_count = 0
					self.stop()
					return 1

				else:
					#hitting head
					#print("hitting head")
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


# -----start of transitions -----

class Event(Enum):
	REGULAR = 1,
	POWERUP = 2,
	DIE = 3


class Normal(State):
	def __init__(self):
		super().__init__(self.__class__.__name__)

	@classmethod
	def update(cls, ant):
		ant.power_down()


class Powered(State):
	def __init__(self):
		super().__init__(self.__class__.__name__)

	@classmethod
	def update(cls, ant):
		ant.power_up()


class Dead(State):
	def __init__(self):
		super().__init__(self.__class__.__name__)

	@classmethod
	def enter(cls, ant):
		ant.dead = True


STATES = [Normal, Powered, Dead]

TRANSITIONS = {
	Event.REGULAR: [Transition(Powered, Normal)],
	Event.POWERUP: [Transition(Normal, Powered)],
	Event.DIE: [
		Transition(Normal, Dead),
	]
}
