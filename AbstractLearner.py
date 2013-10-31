from __future__ import print_function

class AbstractLearner:
	"""
	An 'abstract base class' of sorts that defines the interface for learning from training data.
	Since I didn't want to use python's strange way of actually making abstract base classes,
	derived classes should make a call to this class to access generic logic like reading from 
	files that will be handled here.
	"""
	
	def __init__(self, trainingInputFile, testInputFile, isMachineReadable):
		self.trainingInputFile = trainingInputFile
		self.testInputFile = testInputFile
		self.isMachineReadable = isMachineReadable
		self.trainingData = self.__processTrainingInput()
		self.testData = self.__processTestingInput()

	def __processTrainingInput(self):
		"""
		Read from trainingInputFile and return a list of lists containing the data.
		Since IO is expensive, this function is 'private' although the concept doesn't 
		really exist in Python ... These functions may be consolidated if the data 
		is clean enough
		"""
		mResult = list()
		mData = open(self.trainingInputFile, 'r')
		mLine = mData.readline()
		rowCount = 0
		while mLine:
			mResult.append(list())
			[mResult[rowCount].append(x) for x in mLine.strip().split(',')]
			mLine = mData.readline()
			rowCount += 1
		return mResult

	def __processTestingInput(self):
		"""
		Read from testInputFile and return a list of lists containing the data.
		Since IO is expensive, this function is 'private' although the concept doesn't 
		really exist in Python ...
		"""
		return list()
	
	def __printListofLists(self, mListofLists):
		[print(x) for x in mListofLists]

	def printTrainingInput(self):
		self.__printListofLists(self.trainingData)

	def printTestingInput(self):
		self.__printListofLists(self, self.testData)

	def learn(self):
		print("Error: Directly called the abstract implementation")

	def classify(self):
		print("Error: Directly called the abstract implementation")
