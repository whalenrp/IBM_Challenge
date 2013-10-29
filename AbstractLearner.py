
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
		return list()

	def __processTestingInput(self):
		"""
		Read from testInputFile and return a list of lists containing the data.
		Since IO is expensive, this function is 'private' although the concept doesn't 
		really exist in Python ...
		"""
		return list()

	def learn(self):
		print "Error: Directly called the abstract implementation"

	def classify(self):
		print "Error: Directly called the abstract implementation"
