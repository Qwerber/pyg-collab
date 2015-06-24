from func import add_vector
class Entity:
	def __init__(self, sprite, pos=(0, 0), facing="right", velocity=(0, 0)):
		self._sprite = sprite
		self._pos = pos
		self._facing = facing
		self._velocity = velocity
		self._default_velocity = velocity
		self._health = 100.0
		self._speed_scale = 1.0
	def move(self, facing, velocity=None):
		self._facing = facing
		if velocity is None:
			self._velocity = self._default_velocity
		else:
			self._velocity = velocity
	def stop():
		self._velocity = (0, 0)
	def update(self):
		add_vector(self.pos, self.velocity)
		

class Player(Entity):
	def __init__(self, sprite, pos=(0, 0), facing="right", velocity=(0, 0)):
		# call parent initializer
		Entity.__init__(self, sprite, pos, facing, velocity)
		self._crouching = False

	def attack(self):
		# for animation's sake
		pass

	def crouch(self, speed_scale=0.5):
		self._crouching = True
		self._speed_scale = speed_scale

	def uncrouch(self, speed_scale=1.0):
		self._crouching = False
		self._speed_scale = speed_scale
