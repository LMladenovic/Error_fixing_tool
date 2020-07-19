from subprocess import call
from datetime import datetime
from shutil import copyfile
import os
import sys

# used to avoid writing bytecode, i.e. .pyc files
sys.dont_write_bytecode = True

sys.path.append(os.path.abspath(os.getcwd() + "/utils"))
from parseOutput import *
from errorHandler import *


def compileProgram(filename):
	# trim .c from filename
	executeFile = filename[0: len(filename)-2]
	call(["gcc",  "-g", "-O0", "-Wall", filename , "-o", executeFile])
	return executeFile

def doJob(filename):

	print("################ RUN STARTED ###################\n")	
	executeFile = compileProgram(filename)
	# calling Valgrind tool MEMCHECK
	call(["valgrind", "--tool=memcheck", "--track-origins=yes", "--log-file=ValgrindLOG.txt" , "./" + executeFile])
	errorInfo = parseOutput()
	# contain changes made to file, in order not to make same changes if they have allready made
	history = ['']

	while errorInfo:
		n = len(history)
		# eliminate errors one by one
		for error in errorInfo:
			if isKnownError(error[0:error.find('\n')]):
				eliminateError(error, filename, history)
				print("\n################ RUN FINISHED ###################\n\n")
				break	
		
		# check if koronka made some change, if so continue searching, else exit
		if len(history) > n:	
			print("################ RUN STARTED ###################\n")				
			executeFile = compileProgram(filename)
			call(["valgrind", "--tool=memcheck", "--track-origins=yes", "--log-file=ValgrindLOG.txt" , "./" + executeFile])
			errorInfo = parseOutput()
		else:
			break

	print("\n################ RUN FINISHED ###################\n\n")
	print("Koronka successfully fixed all what were in her power! :)")

def main():
	now = datetime.now()
	current_time = now.strftime("%m%d%Y-%H%M%S")

	###### CREATING WORKING DIRECTORY WHERE SOLUTION WILL BE STORED ######
	directory = os.getcwd() + "/"+ current_time
	try:
    		
		if len(sys.argv)< 2:
			print ("Usage: python koronka.py PROGRAM [arguments]")
		elif not os.path.exists(sys.argv[1]) or not os.path.isfile(sys.argv[1]) :
			print ("Program proceeded as argument [" + sys.argv[1] + "] doesn't exsist or is not a file")
		else:
			os.mkdir(directory)
			
			######  COPYING FILES TO WORKING DIRECTORY ######
			
			# in case we are giving our program as complite path
			filename = sys.argv[1].split('/')[-1:][0] 

			copyfile(sys.argv[1], directory + "/" + filename)
			os.chdir(directory)
			print ("Successfully created the directory "+ directory +" , and moved file " + filename)
			try:
				doJob(filename) 
			
			except OSError:
				print ("Failed to run koronka :(")
	except OSError:
		print ("Creation of the directory %s failed" % directory)
		

if __name__ == "__main__":
	main()

