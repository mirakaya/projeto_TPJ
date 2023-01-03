

class Measures():

	def __init__(self, scale, width, height, display, character_image_dimensions=(0,0)):
		self.scale = scale
		self.width = width
		self.height = height
		self.display = display
		self.character_image_dimensions = character_image_dimensions

	def set_scale(self, new_scale):
		self.scale = new_scale

	def get_scale(self):
		return self.scale

	def set_height(self, new_height):
		self.height = new_height

	def get_height(self):
		return self.height

	def set_width(self, new_width):
		self.width = new_width

	def get_width(self):
		return self.width

	def set_display(self, display):
		self.display = display

	def get_display(self):
		return self.display

	def set_character_image_dimensions(self, width, height):
		self.character_image_dimensions = (width, height)

	def get_character_image_dimensions(self):
		return self.character_image_dimensions