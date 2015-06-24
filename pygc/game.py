import tilemaps, pygame

class Game:

	def __init__(self):
		self.pic = pygame.image.load("../assets/image.png")
		self.tilemap = tilemaps.Tilemap(64,10,10)
		self.tilemap.setTilesheet(self.pic)

	def update(self):
		pass

	def render(self, screen):
		self.tilemap.render(screen)
		pass