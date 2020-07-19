class ErrorInfo:

	# Initialisation with errorType
	def __init__(self, errorType, valgrindOutput, filename):
        	self.errorType = errorType
		self.valgrindOutput = valgrindOutput
		self.filename = filename
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

	def getFilename(self):
		return self.filename

	def getValgrindOutput(self):
		return self.valgrindOutput

	def getErrorReason(self):
		return self.errorReason

	def getProblemLines(self):
		return self.problemLines

	def setProblemLines(self, problemLines):
		self.problemLines=problemLines

	def setErrorReason(self, errorReason):
		self.errorReason= errorReason

	def setBug(self, bug):
		self.bug = bug

	def setBugFix(self, bugFix):
		self.bugFix = bugFix

	def isKnownReason(self, newReason):
		for reason in self.errorReason:
			if reason.find(newReason) >= 0:
				return True
				break

		return False


