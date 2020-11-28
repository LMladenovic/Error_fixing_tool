class ErrorInfo:

	# Initialisation with errorType
	def __init__(self, errorType, valgrindOutput, files):
        	self.errorType = errorType
		self.valgrindOutput = valgrindOutput
		self.files = files
		self.changedFile = ''
		self.changedLine = -1
		self.problemLines = []
		self.errorReason = []
		self.bug = ''
		self.bugFix = ''

	def getErrorType(self):
		return self.errorType

	def getBug(self):
		return self.bug
	
	def getValgrindOutput(self):
		return self.valgrindOutput

	def getBugFix(self):
		return self.bugFix

	def getFiles(self):
		return self.files

	def getValgrindOutput(self):
		return self.valgrindOutput

	def getErrorReason(self):
		return self.errorReason

	def getProblemLines(self):
		return self.problemLines
	
	def getChangedFile(self):
		return self.changedFile
	
	def setChangedFile(self, filename):
		self.changedFile = filename

	def setProblemLines(self, problemLines):
		self.problemLines=problemLines

	def setErrorReason(self, errorReason):
		self.errorReason= errorReason

	def setBug(self, bug):
		self.bug = bug

	def setBugFix(self, bugFix):
		self.bugFix = bugFix

	def setChangedLine(self, lineNumber):
		self.changedLine = lineNumber

	def getChangedLine(self):
		return self.changedLine

	def isKnownReason(self, newReason):
		for reason in self.errorReason:
			if reason.find(newReason) >= 0:
				return True

		return False


