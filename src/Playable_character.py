from enum import Enum
from src.common import *
from src.fsm_characters import *

class Playable_character:

	def __init__(self):
		self.dead = False


	def move(self):
		pass

	def jump(self):
		pass

	def cancel_jump(self):
		pass

	def dash(self):
		pass

	def update(self):
		pass

#-----start of transitions -----

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
