import pygame

class KeyObj:
	pass

key = KeyObj();
key.pressed = []
key.lastPressed = []

def init():
	key.pressed = pygame.key.get_pressed()
	key.lastPressed = pygame.key.get_pressed()

def update():
	key.lastPressed = key.pressed[:]
	key.pressed = pygame.key.get_pressed()

def isPressed(_key):
	return key.pressed[_key]

def justPressed(_key):
	return key.pressed[_key] and not(key.lastPressed[_key])

def justReleased(_key):
	return not(key.pressed[_key]) and key.lastPressed[_key]
