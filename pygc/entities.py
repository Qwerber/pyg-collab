from func import add_vector
class Entity:
	def __init__(self, sprite, pos=(0, 0), facing="right", velocity=(0, 0)):
		self._sprite = sprite
		self._pos = pos
		self._facing = facing
		self._velocity = velocity
	def move(self, facing, velocity):
		self._facing = facing
		self._velocity = velocity
	def update(self):
		add_vector(self.pos, self.velocity)
		

class Player(Entity):
	def __init__(self):
		# call parent initializer
		Entity.__init__(self)
