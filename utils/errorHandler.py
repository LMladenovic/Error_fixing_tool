import fileinput
from errorClass import *
from uninitialisedFix import *
from invalidFreeFix import *
import re
from invalidReadOrWriteFix import *

errorType = [
	'Conditional jump or move depends on uninitialised value(s)',
	'Use of uninitialised value of size ',
	'Invalid free() / delete / delete[] / realloc()',
	'Invalid read of size ',
	'Invalid write of size '
]

errorReason = [
	'Uninitialised value was created by a stack allocation',
	'Uninitialised value was created by a heap allocation',
	' bytes after a block of size '

]

# function which will check if Valgrinds output error can be handled and fixed by koronka
def isKnownError(newError):
	for error in errorType:
		if newError.find(error) >= 0:
			return True
			break
	
	return False

def isKnownReason(newReason):
	for reason in errorReason:
		if newReason.find(reason) >= 0:
			return True
			break
	
	return False

def eliminateError(errorInfo, filename, history):
	report = open("ExecutionReport.txt",'a')
	report.write('#####  Based on Valgrind output:  #####\n\n')
	report.write(errorInfo)	
	
	report.write('\n#####  Koronka made following changes in ' + filename + '  #####\n\n')

	# define error and decide what to do to fix it 	
	err = ErrorInfo(errorInfo[0:errorInfo.find('\n')], errorInfo, filename)
	updateErrInfo(err)
	
	fix(err, history)

	if err.getBug() and err.getBugFix():
		# change in file what shoud be changed
		f = open(filename,'r')
		data = f.readlines()
		f.close()

		# change bug in code found by koronka
		data[err.getChangedLine() -1] = err.getBugFix()

		f = open(filename,'w')
		for line in data:
			f.write(line)
		f.close()

	if err.getBug() and err.getBugFix():
		report.write('Changed ' + str(err.getChangedLine()) + '. line \n' + err.getBug() + ' with \n' + err.getBugFix() + '\n\n')
	elif err.getBug():
		report.write('Removed ' + str(err.getChangedLine()) + '. line\n' + err.getBug() + '\n\n')
	
	report.close()


def updateErrInfo(err):
	filename = err.getFilename()

	outputLines = err.getValgrindOutput().split('\n')
	# contain informations about explicit reason which caused error
	currentErrorReason = []
	lineNumbers = []

	for line in outputLines:
		if isKnownReason(line):
			currentErrorReason.append(line)
		if line.find(filename) >=0:
			# last number in set is number of line in file with given filename
			lineNumbers.append(int(re.findall(r'\d+', line)[-1:][0]))
	
	lineNumbers = lineNumbers[::-1]		

	err.setProblemLines(lineNumbers)
	err.setErrorReason(currentErrorReason)

def fix(err, history):

	# fix error caused by uninitialised variable
	if err.getErrorType() == 'Conditional jump or move depends on uninitialised value(s)' and \
	 'Uninitialised value was created by a stack allocation' in err.getErrorReason():
		uninitialisedStaticVariable(err, history)

	# fix error caused by uninitialised dinamiclly allocated variable
	if err.getErrorType() == 'Conditional jump or move depends on uninitialised value(s)' and \
	 'Uninitialised value was created by a heap allocation' in err.getErrorReason():
		uninitialisedDinamicllyAllocatedVariable(err, history)

	# invalid free
	if err.getErrorType() == 'Invalid free() / delete / delete[] / realloc()':
		invalidFree(err, history)

	#invalid read or write
	if err.getErrorType().find( 'Invalid read of size')>=0 and err.isKnownReason(' bytes after a block of size '):
		invalidReadOrWriteFix(err, history)

	if err.getErrorType().find( 'Invalid write of size')>=0 and err.isKnownReason(' bytes after a block of size '):
		invalidReadOrWriteFix(err, history)



