import pygame

class Tilemap():
	def __init__(self, tilesize, width, height):
		
		self.tilesize = tilesize
		self.width = width
		self.height = height
		self.tilesheet = None
		self.data = [0 for x in range(self.width * self.height)]

	def setTilesheet(self, tilesheet):
		self.tilesheet = tilesheet

	def render(self, screen):
		screen.blit(self.tilesheet, (0,0))
		pass