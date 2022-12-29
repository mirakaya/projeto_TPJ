from enum import Enum
from src.common import *
from src.fsm_characters import *
from src.inputs import Up, Down, Left, Right

ACC = 0.5
vec = pygame.math.Vector2  # 2 for two dimensional

velocity = 0.1


class Playable_character(Actor, Subject):

	def __init__(self, measures, name=None, init_pos=(0, 0)):
		Subject.__init__(self)
		self.name = name
		self.direction = Directions.DOWN
		self.dead = False
		self.control_keys = dict()
		self.measures = measures
		self.pos = vec(init_pos)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)
		self.jumping = False

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

	def move_right(self):
		self.vel.x = velocity
		self.pos += self.vel

	def move_left(self):
		self.vel.x = -velocity
		self.pos += self.vel


	def jump(self):
		self.vel = vec(0, 0.1)

		hits = self.colliding()
		#if hits:
			# self.jumping = True
			#self.vel.y = -self.vel.y
		self.vel.y = -self.vel.y
		self.pos += self.vel

	def cancel_jump(self):
		self.vel = vec(0, 0.1)

		hits = self.colliding()

		# TODO - tmp comment
		'''if self.jumping == False:
			self.jumping = True
			self.vel.y = self.vel.y'''
		self.vel.y = self.vel.y
		self.pos += self.vel

	'''def update(self):
		#hits = pygame.sprite.spritecollide(self, platforms, False)
		if self.vel.y > 0:
			if hits:
				if self.pos.y < hits[0].rect.bottom:
					if hits[0].point == True:
						hits[0].point = False
						self.score += 1
					self.pos.y = hits[0].rect.top + 1
					self.vel.y = 0
					self.jumping = False'''

	def colliding(self):

		r = pygame.Rect(self.measures.get_scale() * self.pos.x,
		    self.measures.get_scale() * self.pos.y,
            self.measures.get_character_image_dimensions()[0],
            self.measures.get_character_image_dimensions()[1]
        )

		hits = r.collidelist(solids)

		'''if hits != []: #there is a collision

			#find on which sides
			self.collision[0] = rect.collidepoint(self.rect.midbottom)
'''

		print("Hits - ", hits)

		'''if hits == 1:
			print(r)'''
		return hits

	def handle_vertical_collision(self):
		collided_objects = []

		'''for obj in solids:
			if pygame.sprite.collide_mask()'''


'''	def jump(self):
		pass

	def cancel_jump(self):
		pass

	def dash(self):
		pass

	def update(self):
		pass'''


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
