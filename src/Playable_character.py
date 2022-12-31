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

		self.rect = pygame.Rect((0,0), (0,0))
		self.character_dimensions = pygame.math.Vector2(0, 0)


	def controls(self, up, left, down, right):
		self.control_keys = {up: Up, left: Left, down: Down, right: Right}

	def command(self, control):
		if control in self.control_keys.keys():
			cmd = self.control_keys[control]()
			cmd.execute(self)
			return cmd

	def move(self, direction: Directions = None):

		if direction == Directions.LEFT:
			self.vel.x = -self.velocity_value

		if direction == Directions.RIGHT:
			self.vel.x = self.velocity_value

		print(self.new_horizontal_collision(solids))
		if self.new_horizontal_collision(solids) == False:
			self.pos.x += self.vel.x






	def jump(self):

		self.jumping = True

		if self.jump_count < self.max_jump_val:
			self.vel.y = -self.velocity_value


		else: #falling
			self.vel.y = self.velocity_value


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

	def new_horizontal_collision(self, object):

		aux_rect = pygame.Rect(self.measures.get_scale() * self.pos.x + 2 * self.vel.x,
		                       self.measures.get_scale() * self.pos.y - self.vel.y,
		                       self.character_dimensions.x,
		                       self.character_dimensions.y)

		for i in object:
			if pygame.Rect.colliderect(aux_rect, i) :
				return True

		return False



	def handle_collision(self, object):

		hitting = False

		aux_rect = pygame.Rect(self.measures.get_scale() * self.pos.x + 3 * self.vel.x,
			self.measures.get_scale() * self.pos.y + 3 * self.vel.y,
			self.character_dimensions.x,
			self.character_dimensions.y)
		#aux_rect = self.rect

		print("pos y -> ", self.pos)
		for i in object:

			if pygame.Rect.colliderect(aux_rect, i):

				if hitting == False:

					hitting = True
					#print(hitting)

					self.character_correction = True
					print(self.vel)

					print("before trans -> ", self.pos)

					if self.vel.x != 0:
						self.horizontal_collision(i)

					print("after x -> ", self.pos)

					if self.vel.y != 0:
						self.vertical_collision(i)

					print("after x y -> ", self.pos)

			if hitting == True:
				break

		if hitting == False: #am flying, no collision
			self.stop()

		return hitting




	def vertical_collision(self, collided_obj):
		if self.vel.y > 0:
			print("vertical t")

			self.pos.y = (collided_obj.top / self.measures.get_scale()) - 1
			self.rect = pygame.Rect(self.measures.get_scale() * self.pos.x,
			                        self.measures.get_scale() * self.pos.y,
			                        self.character_dimensions.x,
			                        self.character_dimensions.y)

			self.jumping = False
			self.jump_count = 0
			print("y -> ", self.pos)
		elif self.vel.y < 0:
			print("vertical b")
			self.pos.y = (collided_obj.top / self.measures.get_scale()) + 1
			self.rect = pygame.Rect(self.measures.get_scale() * self.pos.x,
			                        self.measures.get_scale() * self.pos.y,
			                        self.character_dimensions.x,
			                        self.character_dimensions.y)

			self.jump_count = self.max_jump_val


	def horizontal_collision(self, collided_obj):
		if self.vel.x > 0:
			print("->", self.pos.x)

			#self.character.pos.x = (collided_obj.left / self.character.measures.get_scale()) - 1
			#print(self.character.pos.x)
			self.rect = pygame.Rect(self.measures.get_scale() * self.pos.x,
			                        self.measures.get_scale() * self.pos.y,
			                        self.character_dimensions.x,
			                        self.character_dimensions.y)
			#self.character.jump_count = self.character.max_jump_val


		elif self.vel.x < 0:
			print("<-", self.pos.x)
			#self.character.pos.x = (collided_obj.right / self.character.measures.get_scale())
			#print(self.character.pos.x)
			self.rect = pygame.Rect(self.measures.get_scale() * self.pos.x,
			                        self.measures.get_scale() * self.pos.y,
			                        self.character_dimensions.x,
			                        self.character_dimensions.y)
			#self.character.jump_count = self.character.max_jump_val



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
