from func import add_vector
class Entity:
	def __init__(self, sprite, pos=(0, 0), facing="right", default_velocity=(0, 0)):
		self._sprite = sprite
		self._pos = pos
		self._facing = facing
		self._default_velocity = default_velocity
		self._velocity = 0.0
		self._health = 100.0
		self._speed_scale = 1.0
	def move(self, facing, velocity=None):
		self._facing = facing
		if velocity is None:
			self._velocity = self._default_velocity
		else:
			self._velocity = velocity
	def stop(self):
		self._velocity = (0, 0)
	def hurt(self, damage):
		self._health -= damage
	def update(self):
		self.pos = add_vector(self.pos, self.velocity)
		

class Player(Entity):
	def __init__(self, sprite, attack_sprite, pos=(0, 0), facing="right", default_velocity=(2, 0)):
		# call parent initializer
		Entity.__init__(self, sprite, pos, facing, default_velocity)
		self._crouching = False
		self._attack_sprite = attack_sprite

	def attack(self):
		# for animation's sake
		pass

	def crouch(self, speed_scale=0.5):
		self._crouching = True
		self._speed_scale = speed_scale

	def uncrouch(self, speed_scale=1.0):
		self._crouching = False
		self._speed_scale = speed_scale
