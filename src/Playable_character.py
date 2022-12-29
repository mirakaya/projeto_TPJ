from enum import Enum
from src.common import *
from src.fsm_characters import *
from src.inputs import Up, Down, Left, Right

ACC = 0.5
vec = pygame.math.Vector2  # 2 for two dimensional

velocity = 0.5


class Playable_character(Actor, Subject):

	def __init__(self, measures, name=None, init_pos=(0, 0)):
		Subject.__init__(self)
		self.GRAVITY = 0.1
		self.name = name
		self.direction = Directions.DOWN
		self.dead = False
		self.control_keys = dict()
		self.measures = measures
		self.pos = vec(init_pos)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)
		self.jumping = False
		self.animation_count = 0
		self.jump_count = 0
		self.max_jump_val = 5
		self.fall_count = 0
		self.character_correction = False

	def controls(self, up, left, down, right):
		self.control_keys = {up: Up, left: Left, down: Down, right: Right}

	def command(self, control):
		if control in self.control_keys.keys():
			cmd = self.control_keys[control]()
			cmd.execute(self)
			return cmd

	def move(self, direction: Directions = None):
		if direction == Directions.LEFT:
			self.move_left()

		if direction == Directions.RIGHT:
			self.move_right()

		self.vel.x = 0


	def move_right(self):
		self.vel.x = velocity
		self.pos += self.vel


	def move_left(self):
		self.vel.x = -velocity
		self.pos += self.vel


	def jump(self):

		self.jumping = True

		if self.jump_count < self.max_jump_val:
			self.vel.y = -velocity
			self.pos += self.vel
			self.jump_count += 1

		else: #falling
			self.vel.y = velocity
			self.pos += self.vel


	def cancel_jump(self):
		self.vel.y = 2 * velocity
		self.pos += self.vel



'''

	def dash(self):
		pass

'''


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
