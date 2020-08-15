from subprocess import call
from datetime import datetime
from shutil import copyfile, rmtree
import os
import sys
import re

# used to avoid writing bytecode, i.e. .pyc files
sys.dont_write_bytecode = True

sys.path.append(os.path.abspath(os.getcwd() + "/utils"))
from parseOutput import *
from errorHandler import *

def copyNecessaryFiles(directory, filePath, fileList):
	# filePath possibly contains path to necessary files
	# fileList contain list of necessary files
	path = ''	
	if filePath.rfind('/'):
		path = filePath[0:filePath.rfind('/')+1]
	files = fileList[fileList.find('[')+1::]
	files = files[0:files.rfind(']')]
	files = files.split(',')
	for file in files:
		if os.path.exists(path + file.strip()):
			if os.path.isfile(path + file.strip()):		
				copyfile(path + file.strip(), directory + "/" + file.strip())
				print ("Successfully moved file " + file.strip())
			else:
				print("The proceeded argument [" + file.strip() + "] is not a file.")
		else:
			print ("The file proceeded as argument [" + path + file.strip() + \
				"] doesn't exist or is not a file.")
			return (0, [])
	return (1, files)

def parseSturctures(structArgs):
	structures = structArgs[structArgs.find('[')+1::]
	structures = structures[0:structures.rfind(']')]
	structures = structures.split(',')
	for struct in structures:
		struct = struct.strip()
	return (1, structures)	

def parseArguments(directory):
	fileNamePosition = -1
	filename = ''
	clArguments='' 
	files= [] 
	structures= [] 
	indicator= 1
 	# detect main file, make working directory and copy the file
	for i in range(1, len(sys.argv)):
		if not re.search('files=\[.*\]', sys.argv[i]) and not re.search('structures=\[.*\]', sys.argv[i]):
			if not os.path.exists(sys.argv[i]) or not os.path.isfile(sys.argv[i]) :
				print ("The program proceeded as argument [" + sys.argv[i] + "] doesn't exist or is not a file.")
				indicator = 0
				break
			else:
				os.mkdir(directory)			
				filename = sys.argv[i].split('/')[-1:][0]
				copyfile(sys.argv[i], directory + "/" + filename)
				print ("Successfully created the directory "+ directory +" , and moved file " + filename)
				fileNamePosition = i
				break

	if not indicator:
		return ('', '', [], [], 0)

	# parse files and structures arguments
	for i in range(1, fileNamePosition):
		if not indicator:
			break
		if re.search('files=\[.*\]', sys.argv[i]):
			(indicator, files) = copyNecessaryFiles(directory, sys.argv[fileNamePosition], sys.argv[i])
		if re.search('structures=\[.*\]', sys.argv[i]):
			(indicator, structures) = parseSturctures(sys.argv[i])	

	if not indicator:
		return ('', '', [], [], 0)
	
	# parse main program arguments 
	for i in range(fileNamePosition+1, len(sys.argv)):
		clArguments += sys.argv[i] + ' '

	return (filename, clArguments, files, structures, indicator)
							

def compileProgram(filename):
	# trim .c from filename
	executeFile = filename[0: len(filename)-2]
	call(["gcc",  "-g", "-O0", "-Wall", filename , "-o", executeFile])
	return executeFile

def doJob(filename, files, clArguments):

	print("################ RUN STARTED ###################\n")	
	executeFile = compileProgram(filename)
	# calling Valgrind tool MEMCHECK
	call(["valgrind", "--tool=memcheck", "--track-origins=yes", "--log-file=ValgrindLOG.txt" , "./" + executeFile, clArguments])
	errorInfo = parseOutput()
	# contain changes made to file, in order not to make same changes if they have allready made
	history = [('',-1,'')]

	while errorInfo:
		n = len(history)
		# eliminate errors one by one
		for error in errorInfo:
			if isKnownError(error[0:error.find('\n')]):
				eliminateError(error, files, history)
				if len(history)>n:
					print("\n################ RUN FINISHED ###################\n\n")
					break	
		
		# check if koronka made some change, if so continue searching, else exit
		if len(history) > n:	
			print("################ RUN STARTED ###################\n")				
			executeFile = compileProgram(filename)
			call(["valgrind", "--tool=memcheck", "--track-origins=yes", "--log-file=ValgrindLOG.txt" ,\
			 "./" + executeFile, clArguments])
			errorInfo = parseOutput()
		else:
			break
	
	print("\n################ RUN FINISHED ###################\n\n")
	print("Koronka successfully fixed all that were in her power! :)")

def main():
	now = datetime.now()
	current_time = now.strftime("%m%d%Y-%H%M%S")

	###### CREATING WORKING DIRECTORY WHERE SOLUTION WILL BE STORED ######
	directory = os.getcwd() + "/"+ current_time
	try:
    		
		if len(sys.argv)< 2:
			print ("Usage: python koronka.py [files=[list of files]] [structures=[list of user defined structures]] \
				 PROGRAM [arguments]")
			return
		else:
						
			######  COPYING FILES TO WORKING DIRECTORY AND PARSE OTHER ARGUMENTS  ######
			(filename, clArguments, files, structures, indicator) = parseArguments(directory)
			files.append(filename)			
			try:
				if indicator:
					os.chdir(directory)
					doJob(filename, files[::-1], clArguments)
				else:
					if os.path.exists(directory):
						rmtree(directory) 
			
			except OSError:
				print ("Failed to run koronka :(")
	except OSError:
		print ("Creation of the directory %s failed" % directory)
		

if __name__ == "__main__":
	main()

