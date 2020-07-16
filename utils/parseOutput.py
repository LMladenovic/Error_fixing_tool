import os
import re 
from errorHandler import *

# function which will handle Valgrind output file and extract all informations about known error types
def parseOutput():
	# os.getcwd() vraca tekuci radni direktorijum pa ce putanja biti os.getcwd() + "/" + "ValgrindLOG.txt"
	f = open(os.getcwd() + "/" + "ValgrindLOG.txt", "r")	
	#f = open(os.getcwd()+"/utils/" + "ValgrindLOG.txt", "r")

	# indicator for the state of known error on not
	indicator = 0
	numberOfErrors = 0
	errorString = ""
	outputInfo = []

	for line in f:
		line = line[re.compile('==[0-9]+== ').match(line).end() : len(line)].strip()
		
		# we got all informations about error, wa are pushing it in outputInfo and continue to look forward
		if not line and indicator:
			indicator = 0
			outputInfo.append(errorString)
			errorString = ""

		# we got new error which is known
		if isKnownError(line):
			indicator = 1
			errorString += line + '\n'
		# we are in state of known error, we are appending information about it 
		elif indicator:
			errorString += line + '\n'
		
	f.close()

	#print(outputInfo[0].split('\n'))
	return outputInfo


