import fileinput
from errorClass import *
from uninitialisedFix import *
from invalidFreeFix import *
import re
from invalidReadOrWriteFix import *
from fishyArgumentFix import *

errorType = [
	'Conditional jump or move depends on uninitialised value(s)',
	'Use of uninitialised value of size ',
	'Invalid free() / delete / delete[] / realloc()',
	'Invalid read of size ',
	'Invalid write of size ',
	' has a fishy (possibly negative) value:'
]

errorReason = [
	'Uninitialised value was created by a stack allocation',
	'Uninitialised value was created by a heap allocation',
	' bytes after a block of size ',
	'is not stack\'d, malloc\'d or (recently) free\'d',
	' bytes before a block of size '

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

def eliminateError(errorInfo, files, structures, history):
	report = open("ExecutionReport.txt",'a')

	# define error and decide what to do to fix it 	
	err = ErrorInfo(errorInfo[0:errorInfo.find('\n')], errorInfo, files)
	updateErrInfo(err)
	
	fix(err, files, structures, history)

	if err.getBug():
		report.write('#####  Based on Valgrind output:  #####\n\n')
		report.write(errorInfo)	
		report.write('\n#####  Koronka made following changes in ' + err.getChangedFile() + '  #####\n\n')

	if err.getBug() and err.getBugFix():
		# change in file what shoud be changed
		f = open(err.getChangedFile(),'r')
		data = f.readlines()
		f.close()

		# change bug in code found by koronka
		data[err.getChangedLine() -1] = err.getBugFix()

		f = open(err.getChangedFile(),'w')
		for line in data:
			f.write(line)
		f.close()

	if err.getBug() and err.getBugFix():
		report.write('Changed ' + str(err.getChangedLine()) + '. line \n' + err.getBug() + ' with \n' + err.getBugFix() + '\n\n')
	elif err.getBug():
		report.write('Removed ' + str(err.getChangedLine()) + '. line\n' + err.getBug() + '\n\n')
	
	report.close()


def updateErrInfo(err):
	files = err.getFiles()

	outputLines = err.getValgrindOutput().split('\n')
	# contain informations about explicit reason which caused error
	currentErrorReason = []
	lineNumbers = []

	for line in outputLines:
		if isKnownReason(line):
			currentErrorReason.append(line)
		for file in files:
			if line.find(file) >=0:
				# last number in set is number of line in file with given filename
				lineNumbers.append((file, int(re.findall(r'\d+', line)[-1:][0])))
	
	lineNumbers = lineNumbers[::-1]		

	err.setProblemLines(lineNumbers)
	err.setErrorReason(currentErrorReason)

def fix(err, files, structures, history):

	# fix error caused by uninitialised variable
	if err.getErrorType() == 'Conditional jump or move depends on uninitialised value(s)' and \
	 'Uninitialised value was created by a stack allocation' in err.getErrorReason():
		uninitialisedStaticVariable(err, files, structures, history)
	
	if err.getErrorType().find('Use of uninitialised value of size ')>=0 and \
	err.isKnownReason('Uninitialised value was created by a stack allocation'):
		uninitialisedStaticVariable(err, files, structures, history)

	# fix error caused by uninitialised dinamiclly allocated variable
	if err.getErrorType() == 'Conditional jump or move depends on uninitialised value(s)' and \
	 'Uninitialised value was created by a heap allocation' in err.getErrorReason():
		uninitialisedDinamicllyAllocatedVariable(err, files, structures, history)

	# invalid free
	if err.getErrorType() == 'Invalid free() / delete / delete[] / realloc()':
		invalidFree(err, files, history)

	#invalid read or write
	if err.getErrorType().find( 'Invalid read of size')>=0 and err.isKnownReason(' bytes after a block of size '):
		invalidReadOrWriteFix(err, files, history)

	if err.getErrorType().find( 'Invalid write of size')>=0 and err.isKnownReason(' bytes after a block of size '):
		invalidReadOrWriteFix(err, files, history)

	if err.getErrorType().find( 'Invalid read of size')>=0 and err.isKnownReason(' bytes before a block of size '):
		leftSideInvalidReadOrWriteFix(err, files, history)

	if err.getErrorType().find( 'Invalid write of size')>=0 and err.isKnownReason(' bytes before a block of size '):
		leftSideInvalidReadOrWriteFix(err, files, history)

	if err.getErrorType().find(' has a fishy (possibly negative) value:')>=0:
		fishyArgumentFix(err, files, history)

	# need to comment the line 
	if err.getErrorType().find('Invalid read of size')>=0 and err.isKnownReason('is not stack\'d, malloc\'d or (recently) free\'d'):
		f = open(err.getProblemLines()[0][0], "r")
		data = f.readlines()
		f.close()
		err.setChangedFile(err.getProblemLines()[0][0])
		err.setChangedLine(err.getProblemLines()[0][1])	
		err.setBugFix('//' + data[err.getChangedLine()-1])
		err.setBug(data[err.getChangedLine()-1])
		if (err.getBugFix(), err.getChangedLine(), err.getChangedFile()) not in history:
			history.append((err.getBugFix(), err.getChangedLine(), err.getChangedFile()))



