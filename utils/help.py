def getHelpText():
	print('Koronka - error fixing tool')
	print('Run program by typing:')
	print('') 
	print( 'python koronka.py [files=[list of files]] [structures=[list of user defined structures]] \
[c file|path to c file] [other arguments]')
	print('') 
	print('[other arguments] - C program command line arguments')
	print('[files = [list of files]] - additional files required by the program (e.g .h files)')
	print('[structures=[list of user defined structures]] - user defined structures (e.g Tree node)')
	print('')
	print('If your program is contained of multiple files, if you don\'t pass them by files=[] argument, \
Koronka won\'t be able to run, because of missing neccessary data.')
	print('If your program contains user defined structures, if you don\'t pass them by structures=[] argument, \
Koronka won\'t be able to fix bugs related to that structures.')
