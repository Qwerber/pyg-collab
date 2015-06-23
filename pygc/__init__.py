import ConfigParser

def main():
	cfg = ConfigParser.ConfigParser()
	cfg.read('settings/gamecfg.ini')

	screenW = cfg.getint('Game', 'screenW')
	screenH = cfg.getint('Game', 'screenH')

	#
	print screenW, screenH

main()