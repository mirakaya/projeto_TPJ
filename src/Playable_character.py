from enum import Enum
from src.common import *
from src.fsm_characters import *
from src.inputs import Up, Down, Left, Right




class Playable_character(Actor, Subject):

	def __init__(self, measures, name=None, init_pos=(0, 0)):
		Subject.__init__(self)
		self.name = name
		self.dead = False
		self.control_keys = dict()
		self.measures = measures
		self.pos = pygame.math.Vector2(init_pos)
		self.vel = pygame.math.Vector2(0, 0)
		self.velocity_value = 0.5
		self.jumping = False
		self.jump_count = 0
		self.max_jump_val = 10
		self.prev_pos = pygame.math.Vector2(0,0)


	def controls(self, up, left, down, right):
		self.control_keys = {up: Up, left: Left, down: Down, right: Right}

	def command(self, control):
		if control in self.control_keys.keys():
			cmd = self.control_keys[control]()
			cmd.execute(self)
			return cmd

	def move(self, direction: Directions = None):

		print("prev - ", self.prev_pos)

		self.prev_pos = self.pos

		print("prev2 - ", self.prev_pos)

		if direction == Directions.LEFT:
			self.vel.x = -self.velocity_value

		if direction == Directions.RIGHT:
			self.vel.x = self.velocity_value

		self.pos.x += self.vel.x

		print("me - ", self.prev_pos , self.pos)

	def jump(self):

		self.jumping = True

		self.prev_pos = self.pos

		if self.jump_count < self.max_jump_val:
			self.vel.y = -self.velocity_value
			self.pos.y += self.vel.y

		else: #falling
			self.vel.y = self.velocity_value
			self.pos.y += self.vel.y

		self.jump_count += 1


	def cancel_jump(self):

		self.prev_pos = self.pos

		self.vel.y = 2 * self.velocity_value
		self.pos.y += self.vel.y


	def dash(self):
		self.vel.x = 4 * self.vel.x
		self.vel.y = 4 * self.vel.y
		self.pos += self.vel

	def stop(self):
		self.vel.x = 0
		self.vel.y = 0



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
