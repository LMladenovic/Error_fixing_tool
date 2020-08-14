import re

def invalidFree(err, files, history):
	filename = err.getProblemLines()[len(err.getProblemLines())-1][0]
	err.setChangedFile(filename)
	f = open( filename, "r")
	data = f.readlines()	
	f.close()
	problemLine = data[err.getProblemLines()[len(err.getProblemLines())-1][1] - 1]
	err.setChangedLine(err.getProblemLines()[len(err.getProblemLines())-1][1])
	err.setBug(problemLine)
	
	get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if y[0].find(x) != -1]
	number = len(get_indexes(problemLine.strip() ,history))
	
	if number:
		history.append((str(number+1) + '. ' + problemLine.strip(), err.getChangedLine(), err.getChangedFile()))
	else:
		history.append(('1. ' + problemLine.strip(), err.getChangedLine(), err.getChangedFile()))
	
	data[err.getProblemLines()[len(err.getProblemLines())-1][1] - 1]= '\n'

	f = open(filename, "w")
	for line in data:
		f.write(line)

	f.close()
