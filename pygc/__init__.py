import ConfigParser, pygame, key, datetime, time
import sys

class Object():
	pass

localVals = Object
localVals.cfg = None
localVals.screen = None
localVals.key = None

msleep = lambda x: time.sleep(x/1000000.0)

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
	localVals.screen = pygame.display.set_mode(size)

def mainloop():
	while True:
		startTime = datetime.datetime.now()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		localVals.key.update()
		#entry point

		endTime = datetime.datetime.now()
		delta = int((endTime - startTime).total_seconds() * 1000)

		if(delta < 16): msleep(16.-delta)


def main():
	readcfg()
	initpyg()
	localVals.key = key.KeyObj();
	mainloop()

main()
