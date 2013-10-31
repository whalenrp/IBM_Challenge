import sys
from AbstractLearner import AbstractLearner

class RandomForestLearner(AbstractLearner):
	"""
	Derived class implementation of AbstractLearner. This class implements the learn() 
	and classify() functions using a Random Forest
	"""

	def __init__(self, trainingInputFile, testInputFile, isMachineReadable, outputFile):
		AbstractLearner.__init__(self, trainingInputFile, testInputFile, 
			isMachineReadable, outputFile)

	def learn(self):
		print "Function not yet Defined"
		sys.exit(0)

	def classify(self):
		print "Function not yet Defined"
		sys.exit(0)
		
