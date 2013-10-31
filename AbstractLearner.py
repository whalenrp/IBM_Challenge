from __future__ import print_function

class AbstractLearner:
	"""
	An 'abstract base class' of sorts that defines the interface for learning from training data.
	Since I didn't want to use python's strange way of actually making abstract base classes,
	derived classes should make a call to this class to access generic logic like reading from 
	files that will be handled here.
	"""
	
	def __init__(self, trainingInputFile, testInputFile, isMachineReadable, outputFile):
		"""
		trainingInputFile - the string filename for training data input
		testInputFile     - the string filename for testing data input
		isMachineReadable - boolean
		outputFile        - the string filename for output
		trainingData      - a list of lists read from trainingInputFile. Each element 
			of this list is a list containing every element of the i'th row
		testData          - same as trainingData but for test evaluation data
		"""
		self.trainingInputFile = trainingInputFile 
		self.testInputFile = testInputFile
		self.isMachineReadable = isMachineReadable
		self.outputFile = outputFile
		self.trainingData = self.__processFileInput(self.trainingInputFile)
		self.testData = self.__processFileInput(self.testInputFile)
		self.headerList = list()

	def __processFileInput(self, filename):
		"""
		Read from trainingInputFile and return a list of lists containing the data.
		Since IO is expensive, this function is 'private' and should not be called except in
		constructors.
		"""
		mResult = list()
		mData = open(filename, 'r')

		""" If the first character in the file is '*', save the first row for header info """
		firstChar = mData.read(1)
		if firstChar is '*':
			self.headerList = mData.readLine().strip().split()
		else:
			mData.seek(0)
		

		""" Loop over the file, reading in a line and making every row into a list. """
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
