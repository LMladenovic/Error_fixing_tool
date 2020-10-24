import re
from initialisationUtils import *

def initialiseUserStructureUsingLoop(varType, variable, length, expressionData, inl, files, structures, history ):
	count = 0
	addition = inl
	index = []
	
	for line in history:
		searchLine = line[0]
		while re.findall('int __index__', searchLine):
			
			searchLine = searchLine[searchLine.find('int __index__')+len('int __index__'):]
			count += 1

	for i in range(0,length):
		if count:
			addition += 'int __index' + str(count+1) + '__;\n' + inl
			index.append( '__index' + str(count+1) + '__')
			count +=1
		else:
			addition += 'int '+ '__index__' +';\n' + inl
			index.append( '__index__')
			count += 1
		
	if re.findall('[a-zA-Z]+', inl):
		inl = ''

	addition = addition[0:addition.rfind(inl)]

	for i in range(0,length):
		if not re.findall('[a-zA-Z]+', expressionData[i]):
			expressionData[i] = str(int(eval(expressionData[i])))

		for j in range(0,i+1):
			addition += inl

		addition += 'for( '+ index[i] +' = 0; ' + index[i] +' < ' + expressionData[i] + '; ' \
			+ index[i] + ' ++)\n'

	for i in range(0,length+1):
		addition += inl
	
	arrayIndex = ''
	for i in range(0,length):
		arrayIndex += '[' + index[i] + ']'

	addition += initialiseStructure(varType, variable.strip() + arrayIndex , inl, files, structures, history)

	# indent unindented lines
	start = -1	
	elements = addition.split('\n')	
	for i in range(0,len(elements)):
		if elements[i].find('for(')>=0:
			elements[i] = elements[i] + '{'
		if elements[i].find(variable.strip() + arrayIndex + '.')>=0:
			start = i+1;
			inl = elements[i][0:elements[i].find(variable.strip())-1]
			break

	for i in range(i+1,len(elements)):
		elements[i] = inl + elements[i]

	newAddition = ''
	for element in elements:
		newAddition+= element + '\n'
	newAddition += inl[0:len(inl)-1] + '}\n'

	return newAddition		

def initialiseStructure(varType, mainVariable, inl, files, structures, history):
	structData = []
	
	# find definition of user defined structure varType
	for file in files:

		f=open(file, 'r')
		data = f.read()
		f.close()
 
		m = re.search('typedef struct [a-zA-z0-9_-\{]+[ ]*([a-zA-z0-9\*\t \n;,_-]+)[ ]*[\}]+[ ]*' + varType.strip() + '[ ]*;' , data)
		if not m:
			m = re.search('typedef struct [ \t]*' + varType.strip() + '[\t {]+[ ]*([a-zA-z0-9\*\t \n;,_-]+)[ ]*[\}]+[ ]*;' , data)
		if m:
			structData = m.group(1).split('\n')
			for elem in structData:
				elem = elem.strip()
				break
	
	addition = ''
	for elem in structData:
		if elem:
			if elem.find('[')>0:
				# array
				m = re.search('([ \t]*)([a-zA-Z_-]+)[ ]+([a-zA-Z0-9_-]+)\[(.+)\].*;', elem)
				if m:
					varType = m.group(2)
					variable = m.group(3)
					expressionData = m.group(4)

					temporaryData = elem[elem.find(m.group(3)):]
					temporaryLen = len(re.findall('\[', temporaryData))
					newExpressionData = []
					for k in range(0,temporaryLen):
						newExpressionData.append(\
						temporaryData[temporaryData.find('[')+1:temporaryData.find(']')])	
						temporaryData = temporaryData[temporaryData.find(']')+1:]
					addition += initialiseUsingLoopForUserStructures(mainVariable, varType, variable, temporaryLen, newExpressionData, inl, history)
			else:
				# simble variable
				m = re.search('([ \t]*)([a-zA-Z_-]+)[ ]+(.+).*;', elem)
				if m:
					if elem[elem.find(m.group(2))::].find('=')<0:
						varType = m.group(2)
						variable=m.group(3)
						if elem.find('*')>=0:
							addition += inl + mainVariable.strip() + '.' + variable + '= NULL;\n'
						elif checkStructure(varType, structures):
							# will be implemented
							print('WILL BE IMPLEMENTED')
						elif initialise(varType)!= 'Invalid':
							addition += inl + mainVariable.strip() + '.' + variable \
								+ '=' + initialise(varType) +';\n'
						else:
							addition = ''
							break

	return addition

# mainVariable is UDS variable, and variable is part of user defined structure element
def initialiseUsingLoopForUserStructures(mainVariable, varType, variable, length, expressionData, inl, history):
	count = 0
	addition = inl
	index = []
	
	for line in history:
		searchLine = line[0]
		while re.findall('int __index__', searchLine):
			
			searchLine = searchLine[searchLine.find('int __index__')+len('int __index__'):]
			count += 1

	for i in range(0,length):
		if count:
			addition += 'int __index' + str(count+1) + '__;\n' + inl
			index.append( '__index' + str(count+1) + '__')
			count +=1
		else:
			addition += 'int '+ '__index__' +';\n' + inl
			index.append( '__index__')
			count += 1
		
	if re.findall('[a-zA-Z]+', inl):
		inl = ''

	addition = addition[0:addition.rfind(inl)]

	for i in range(0,length):
		if not re.findall('[a-zA-Z]+', expressionData[i]):
			expressionData[i] = str(int(eval(expressionData[i])))

		for j in range(0,i+1):
			addition += inl

		addition += 'for( '+ index[i] +' = 0; ' + index[i] +' < ' + expressionData[i] + '; ' \
			+ index[i] + ' ++)\n'

	for i in range(0,length+1):
		addition += inl
	
	arrayIndex = ''
	for i in range(0,length):
		arrayIndex += '[' + index[i] + ']'

	addition += mainVariable.strip() + '.' + variable.strip() + arrayIndex + ' = ' + initialise(varType) + ';\n'

	return addition	



