import ConfigParser, pyg

cfg = None

def readcfg():
	cfg = ConfigParser.ConfigParser()
	cfg.read('settings/gamecfg.ini')

	screenW = cfg.getint('Game', 'screenW')
	screenH = cfg.getint('Game', 'screenH')

	#
	print screenW, screenH

def initpyg():


def main():
	readcfg()
	initpyg()

main()