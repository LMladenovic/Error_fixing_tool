def checkStructure(varType, structures):
	if varType in structures:
		return True
	else:
		return False

def initialise(varType):
	initialisator = {
		'int': '0',
		'double': '0',
		'float': '0',
		'boolean': 'False',
		'char': '\'\\0\''
	    }
	
	if varType in initialisator:
		return initialisator[varType]
	else:
		return 'Invalid'


