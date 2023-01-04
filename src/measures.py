
class Measures(): #measures of the screen and display

	def __init__(self, scale, width, height, display):
		self.scale = scale
		self.width = width
		self.height = height
		self.display = display

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