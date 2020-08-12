from subprocess import call
from datetime import datetime
from shutil import copyfile, copytree
import os
import sys
import re

# used to avoid writing bytecode, i.e. .pyc files
sys.dont_write_bytecode = True

sys.path.append(os.path.abspath(os.getcwd() + "/utils"))
from parseOutput import *
from errorHandler import *

def copyNecessaryFiles(directory):
	# sys.argv[1] possibly contains path to necessary files
	# sys.argv[2] contain list of necessary files
	path = ''	
	if sys.argv[1].rfind('/'):
		path = sys.argv[1][0:sys.argv[1].rfind('/')+1]
	files = sys.argv[2][sys.argv[2].find('[')+1::]
	files = files[0:files.rfind(']')]
	files = files.split(',')
	for file in files:
		if os.path.exists(path + file.strip()):
			if not os.path.isfile(path + file.strip()):
				copytree(path + file.strip(), directory + "/" + file.strip())
				print ("Successfully moved directory " + file.strip())
			else:		
				copyfile(path + file.strip(), directory + "/" + file.strip())
				print ("Successfully moved file " + file.strip())
		else:
			print ("The file proceeded as argument [" + path + file.strip() + \
				"] doesn't exist or is not a file.")
			return 0
	return 1					

def compileProgram(filename):
	# trim .c from filename
	executeFile = filename[0: len(filename)-2]
	call(["gcc",  "-g", "-O0", "-Wall", filename , "-o", executeFile])
	return executeFile

def doJob(filename, clArguments):

	print("################ RUN STARTED ###################\n")	
	executeFile = compileProgram(filename)
	# calling Valgrind tool MEMCHECK
	call(["valgrind", "--tool=memcheck", "--track-origins=yes", "--log-file=ValgrindLOG.txt" , "./" + executeFile, clArguments])
	errorInfo = parseOutput()
	# contain changes made to file, in order not to make same changes if they have allready made
	history = ['']

	while errorInfo:
		n = len(history)
		# eliminate errors one by one
		for error in errorInfo:
			if isKnownError(error[0:error.find('\n')]):
				eliminateError(error, filename, history)
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
	indicator = 1
	now = datetime.now()
	current_time = now.strftime("%m%d%Y-%H%M%S")

	###### CREATING WORKING DIRECTORY WHERE SOLUTION WILL BE STORED ######
	directory = os.getcwd() + "/"+ current_time
	try:
    		
		if len(sys.argv)< 2:
			print ("Usage: python koronka.py [files=[list of files]] PROGRAM [arguments]")
			return
		if re.search('files=\[.*\]', sys.argv[1]):
			tmp = sys.argv[1]
			sys.argv[1]=sys.argv[2]
			sys.argv[2] = tmp
			indicator = 0
		if not os.path.exists(sys.argv[1]) or not os.path.isfile(sys.argv[1]) :
			print ("The program proceeded as argument [" + sys.argv[1] + "] doesn't exist or is not a file.")
			
		else:
			os.mkdir(directory)			

			######  COPYING FILES TO WORKING DIRECTORY ######
			
			# in case we are giving our program as complite path
			filename = sys.argv[1].split('/')[-1:][0] 

			copyfile(sys.argv[1], directory + "/" + filename)
			print ("Successfully created the directory "+ directory +" , and moved file " + filename)
			if not indicator:
				indicator = copyNecessaryFiles(directory)
			os.chdir(directory)

			try:
				clArguments = ''
				for i in range(2+indicator,len(sys.argv)):
					clArguments += sys.argv[i] + ' '
				
				if indicator:
					doJob(filename, clArguments) 
			
			except OSError:
				print ("Failed to run koronka :(")
	except OSError:
		print ("Creation of the directory %s failed" % directory)
		

if __name__ == "__main__":
	main()

