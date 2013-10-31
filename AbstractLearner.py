from __future__ import print_function

class AbstractLearner:
	"""
	An 'abstract base class' of sorts that defines the interface for learning from training data.
	Since I didn't want to use python's strange way of actually making abstract base classes,
	derived classes should make a call to this class to access generic logic like reading from 
	files that will be handled here.
	"""
	
	def __init__(self, trainingInputFile, testInputFile, isMachineReadable, outputFile):
		self.trainingInputFile = trainingInputFile
		self.testInputFile = testInputFile
		self.isMachineReadable = isMachineReadable
		self.outputFile = outputFile
		self.trainingData = self.__processFileInput(self.trainingInputFile)
		self.testData = self.__processFileInput(self.testInputFile)

	def __processFileInput(self, filename):
		"""
		Read from trainingInputFile and return a list of lists containing the data.
		Since IO is expensive, this function is 'private' although the concept doesn't 
		really exist in Python...
		"""
		mResult = list()
		mData = open(filename, 'r')
		mLine = mData.readline()
		rowCount = 0
		while mLine:
			mResult.append(list())
			[mResult[rowCount].append(x) for x in mLine.strip().split(',')]
			mLine = mData.readline()
			rowCount += 1
		return mResult

	def __printListofLists(self, mListofLists):
		[print(x) for x in mListofLists]

	def printTrainingInput(self):
		self.__printListofLists(self.trainingData)

	def printTestingInput(self):
		self.__printListofLists(self.testData)

	def learn(self):
		print("Error: Directly called the abstract implementation")

	def classify(self):
		print("Error: Directly called the abstract implementation")
