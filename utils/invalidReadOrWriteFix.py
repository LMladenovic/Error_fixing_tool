import re

def invalidReadOrWriteFix(err, history):

	f = open( err.getFilename(), "r")
	data = f.readlines()
	f.close()
	
	elemSize = ''
	bytesAfter = ''
	addition = ''
	
	lineToChange = data[err.getProblemLines()[0]-1]
	elemSize = int(re.findall('\d+', err.getErrorType())[0])

	for line in err.getErrorReason():
		if re.findall('Address [0-9a-zA-Z]+ is \d+ bytes after a block of size \d+ alloc\'d', line):
			bytesAfter = int(re.findall('\d+', line.split('is')[1])[0])
			break

	if elemSize and bytesAfter:
		start = lineToChange.find('*')
		end = lineToChange.find('=')
		varType = lineToChange[0:start].strip()
		addition = lineToChange[:lineToChange.rfind(')')] + ' + ' + 'sizeof(' + varType + ')*' \
			+ str((bytesAfter+elemSize)/elemSize) + ' );\n'

		if addition not in history:
			err.setBug(lineToChange)
			err.setBugFix(addition)	
			history.append(addition)	

