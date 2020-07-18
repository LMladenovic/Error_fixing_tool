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
	f.close()
		
	lineCausedProblems = data[err.getProblemLines()[0] - 1]
	addition=''
	
	m = re.search('(malloc|calloc|realloc)(.+);', lineCausedProblems)
	if m:
		expressionData = m.group(2).replace('(', '', 1)[::-1].replace(')', '', 1)[::-1].strip()
		expressionData = re.sub('sizeof[ ]*\([ ]*(int|double|char|float)[ ]*\)', '1' , expressionData)
		start = lineCausedProblems.find('*')
		end = lineCausedProblems.find('=')
		varType = lineCausedProblems[0:start].strip()
		inl = lineCausedProblems[0:start - len(varType) - 1]
		variable = lineCausedProblems[lineCausedProblems.find('*') + 1 : lineCausedProblems.find('=')]
		
		if initialise(varType)!= 'Invalid':
			count = 0
			for line in history:
				if line.find('__index__') > 0 :	
					count += 1

			if count:
				addition = ''
			else:
				addition = 'int '+ '__index__' +';\n'

			if addition:
				addition += inl
			
			addition += 'for( '+ '__index__' +' = 0; ' + '__index__' +' < ' + expressionData + '; ' \
				+ '__index__ ' + ' ++)\n' +inl + '\t' +  variable.strip() + '[' + '__index__' + '] = ' \
				+ initialise(varType) + ';'

	if addition and addition not in history:
		history.append(addition)		
		# addition = problemLine[start:end] + " = " + initialise(varType) + ';'
		# set what should be changed
		err.setBug(lineCausedProblems)
		err.setBugFix(lineCausedProblems + lineCausedProblems.replace(lineCausedProblems.strip() , addition) )




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

