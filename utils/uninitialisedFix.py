import re

def uninitialisedStaticVariable(err, history):
	
	f = open( err.getFilename(), "r")
	data = f.readlines()

	lineCausedProblems = data[err.getProblemLines()[1] - 1]
	addition=''

	check = lineCausedProblems.split("\"")[-1:][0].strip().split(',')
	for item in check:
		# add expression check (i.e. a + b)
		if item.find(')')>=0:			
			item = item[0: item.find(')')].strip()
		else: 
			item = item.strip()
		for i in range(err.getProblemLines()[0], len(data)):		
			if data[i].find(item)>0:			
				# we found line where item is, let's check is that problematic line
				end = data[i].find('=')
				# we have declaration withount initialisation				
				if end < 0:
					start = data[i].find(item)	
					varType = data[i][0:start].strip()
					if initialise(varType)!= 'Invalid':
						addition = data[i].replace(';' , '= ' + initialise(varType) + ';')
						err.setBug(data[i])
						err.setBugFix(addition)	
						break

		if addition not in history:
			history.append(addition)
			break		

	f.close()


def uninitialisedDinamicllyAllocatedVariable(err, history):

	f = open( err.getFilename(), "r")
	data = f.readlines()

	problemLine = data[err.getProblemLines()[0] - 1]
	lineCausedProblems = data[err.getProblemLines()[1] - 1]
	
	start = problemLine.find('*')
	end = problemLine.find('=')
	varType = problemLine[0:start].strip()
	addition=''	

	# printf, write, fprintf, sprintf, etc. may cause this error
	# if lineCausedProblems.find('printf')>=0:

	check = lineCausedProblems.split("\"")[-1:][0].strip().split(',')
	for item in check:
		if item.find(')')>=0:			
			item = item[0: item.find(')')].strip()
		else: 
			item = item.strip()

		# it is not >= because variable type is in front of variable
		if item.find(problemLine[start:end].strip())==0 and  problemLine[start:end].strip().find(item)==0 :
			if initialise(varType)!= 'Invalid':			
				addition = item + " = " + initialise(varType) + ';'			
		elif item.find('[')>=0:
			if problemLine[start:end].strip().find(item[0:item.find('[')]) >=0:
				if initialise(varType)!= 'Invalid':
					addition = item + " = " + initialise(varType) + ';'
			
		if addition not in history:
			history.append(addition)
			break			
				

	# addition = problemLine[start:end] + " = " + initialise(varType) + ';'

	# set what should be changed
	if addition:
		err.setBug(lineCausedProblems)
		err.setBugFix(lineCausedProblems.replace(lineCausedProblems.strip() , addition) + lineCausedProblems )

	f.close()


def initialise(varType):
	initialisator = {
		'int': '0',
		'double': '0',
		'float': '0',
		'boolean': 'False',
		'char': ''
	    }
	
	if varType in initialisator:
		return initialisator[varType]
	else:
		return 'Invalid'

