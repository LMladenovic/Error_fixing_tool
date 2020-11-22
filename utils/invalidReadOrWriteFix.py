import re

def getRegEx():
	return '\(([a-zA-z0-9]*[ ]*\*[ ]*)*[ ]*sizeof[ ]*\(([a-zA-z0-9\* ]*)\)[ ]*(\*[ ]*[a-zA-z0-9]*)*[ ]*[\)\+]'

def invalidReadOrWriteFix(err, files, history):

	for file in files:
		f = open( file, "r")
		data = f.readlines()
		f.close()
		
		elemSize = ''
		bytesAfter = ''
		addition = ''
		
		for elem in err.getProblemLines():
			if re.findall('.+(malloc|calloc|realloc)+.*', data[elem[1]-1]) and elem[0]==file:
				lineToChange = data[elem[1]-1]
				err.setChangedLine(elem[1])
				err.setChangedFile(file)
				elemSize = int(re.findall('\d+', err.getErrorType())[0])
				break

		for line in err.getErrorReason():
			if re.findall('Address [0-9a-zA-Z]+ is \d+ bytes after a block of size \d+ alloc\'d', line):
				bytesAfter = int(re.findall('\d+', line.split('is')[1])[0])
				break

		if elemSize != '' and bytesAfter != '':
			size = str(int((bytesAfter+elemSize)/elemSize)) 
			n = re.search('(malloc|calloc|realloc)', lineToChange)
			if n.group(1)=='malloc':
				m = re.search('\(([a-zA-z0-9]*[ ]*\*[ ]*)*[ ]*sizeof[ ]*\(([a-zA-z0-9\* ]*)\)[ ]*(\*[ ]*[a-zA-z0-9]*)*([ ]*[\)\+])'\
						, lineToChange)

				if m:
					if m.group(1) and m.group(2):
						addition =  '(' + m.group(1) + 'sizeof(' + m.group(2) + ')' + \
						' + ' + size + '*sizeof(' + m.group(2) + ')' + m.group(4)
		
					if m.group(2) and m.group(3):
						addition = '(' + 'sizeof(' + m.group(2) + ')' + m.group(3) + \
							' +' + size + '*sizeof(' + m.group(2) + ')' + m.group(4)

					addition = re.sub(getRegEx(), addition, lineToChange)

			if n.group(1)=='realloc':
				addition = lineToChange[0:lineToChange.find(',')+1]
				m = re.search('sizeof[ ]*\(([a-zA-z0-9\* ]*)\)', lineToChange)
				addition += ' ' + size + '*sizeof(' + m.group(1) + ') + ' + lineToChange[lineToChange.find(',')+1:]
			
			if n.group(1)=='calloc':
				addition = lineToChange[0:lineToChange.find(',')+1]
				addition+= ' ' + size + ' +' + lineToChange[lineToChange.find(',')+1:]

			if (addition, err.getChangedLine(), err.getChangedFile()) not in history:
				
				err.setBug(lineToChange)
				err.setBugFix(addition)	
				history.append((addition, err.getChangedLine(), err.getChangedFile()))
				break	

def leftSideInvalidReadOrWriteFix(err, files, history):
	fileToChange = err.getProblemLines()[1][0]
	numOfLineToChange = err.getProblemLines()[1][1]
	addition = ''

	if fileToChange in files:
		f = open( fileToChange, "r")
		data = f.readlines()
		f.close()
		lineToChange = data[numOfLineToChange-1]
		bufferLine = lineToChange
		addition = ''
		if bufferLine.rfind('\"')>0:
			addition += bufferLine[0:bufferLine.rfind('\"')+1]
			bufferLine = bufferLine[bufferLine.rfind('\"')+1:]
		
		while(bufferLine.find('[')>=0):
			addition += bufferLine[0:bufferLine.find('[')+1]
			addition += 'abs('
			addition += bufferLine[bufferLine.find('[')+1:bufferLine.find(']')]
			addition += ')]'
			bufferLine =  bufferLine[bufferLine.find(']')+1:]
		
		addition += bufferLine

	if addition.find('abs(')>=0:
		err.setChangedLine(numOfLineToChange)
		err.setChangedFile(fileToChange)
		if (addition, err.getChangedLine(), err.getChangedFile()) not in history:
				err.setBug(lineToChange)
				err.setBugFix(addition)	
				history.append((addition, err.getChangedLine(), err.getChangedFile()))