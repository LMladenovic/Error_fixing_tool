import re

def invalidFree(err, history):
	f = open( err.getFilename(), "r")
	data = f.readlines()	
	f.close()
	problemLine = data[err.getProblemLines()[len(err.getProblemLines())-1] - 1]
	err.setBug(problemLine)
	
	get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if y.find(x) != -1]
	number = len(get_indexes(problemLine.strip() ,history))
	
	if number:
		history.append(str(number+1) + '. ' + problemLine.strip())
	else:
		history.append('1. ' + problemLine.strip())
	
	data[err.getProblemLines()[len(err.getProblemLines())-1] - 1]= '\n'

	f = open( err.getFilename(), "w")
	for line in data:
		f.write(line)

	f.close()
		
		
