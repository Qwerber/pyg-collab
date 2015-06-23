import ConfigParser, pygame, key
import sys

class Object():
	pass

localVals = Object
localVals.cfg = None
localVals.screen = None
localVals.key = None

def readcfg():
	localVals.cfg = ConfigParser.ConfigParser()
	localVals.cfg.read('settings/gamecfg.ini')

	screenW = localVals.cfg.getint('Game', 'screenW')
	screenH = localVals.cfg.getint('Game', 'screenH')

	#
	print screenW, screenH

def initpyg():
	pygame.init()

	screenW = localVals.cfg.getint('Game', 'screenW')
	screenH = localVals.cfg.getint('Game', 'screenH')

	size = screenW, screenH
	localVals.screen = pygame.display.set_mode(size);

def mainloop():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		localVals.key.update()
		#entry point


def main():
	readcfg()
	initpyg()
	localVals.key = key.KeyObj();
	mainloop()

main()
