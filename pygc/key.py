import pygame

class KeyObj:
	def __init__(self):
		self.pressed = pygame.key.get_pressed()
		self.lastPressed = pygame.key.get_pressed()
	def update(self):
		self.lastPressed = key.pressed[:]
		self.pressed = pygame.key.get_pressed()

	def isPressed(self, _key):
		return self.pressed[_key]

	def justPressed(self, _key):
		return self.pressed[_key] and not(self.lastPressed[_key])

	def justReleased(self, _key):
		return not(self.pressed[_key]) and self.lastPressed[_key]
