import re

def uninitialisedStaticVariable(err, history):
	
	f = open( err.getFilename(), "r")
	data = f.readlines()
	
	lineCausedProblems = data[err.getProblemLines()[1] - 1]
	addition=''

	check = lineCausedProblems.split("\"")[-1:][0].strip().split(',')
	for item in check:
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
						err.setChangedLine(i+1)
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
	lineCausedProblems = ''
	addition=''

	for elem in err.getProblemLines():
		m = re.search('(malloc|calloc|realloc)(.+);', data[elem-1])
		if m:
			lineCausedProblems = data[elem - 1]
			err.setChangedLine(elem)
			break
	


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
			if not re.findall('[a-zA-Z]+', expressionData) and eval(expressionData) == 1:
				addition = lineCausedProblems[start:end] + " = " + initialise(varType) + ';'
			else:
				count = 0
				for line in history:
					if line.find('__index__') > 0 :	
						count += 1

				if count:
					addition = 'int __index' + str(count) + '__;\n'
					index = '__index' + str(count) + '__'
				else:
					addition = 'int '+ '__index__' +';\n'
					index = '__index__'
				
				if re.findall('[a-zA-Z]+', inl):
					inl = ''

				if addition:
					addition += inl

				if not re.findall('[a-zA-Z]+', expressionData):
					expressionData = str(eval(expressionData))

				addition += 'for( '+ index +' = 0; ' + index +' < ' + expressionData + '; ' \
					+ index + ' ++)\n' +inl + '\t' +  variable.strip() + '[' + index + '] = ' \
					+ initialise(varType) + ';'

	
	if addition and addition not in history:
		history.append(addition)		
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

