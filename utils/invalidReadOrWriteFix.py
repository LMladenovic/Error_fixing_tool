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

			if (addition, err.getChangedLine(), err.getChangedFile()) not in history:
				
				err.setBug(lineToChange)
				err.setBugFix(addition)	
				history.append((addition, err.getChangedLine(), err.getChangedFile()))
				break	

