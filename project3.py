import sys

def main(args):
	"""
	Main should interpret flags passed to the program (i.e. training_input_file, 
	human_readable_classifier, machine_readable_classifier and test_input_file) and write output
	to the specified file (classify_results_file).
	"""

	" Set defaults for command parameters"
	variables = {"trainingInputFile" : "trainingInput.txt", "testInputFile" : "testInput.txt",
		"machineReadable" : True}

	"Define some functions for input processing"
	"They take as a parameter the current command arg index"
	"and return the index after they are done processing"
	def setTrainingInputFile(curArgNum):
		curArgNum += 1
		variables["trainingInputFile"] = sys.argv[curArgNum]
		return curArgNum

	def setHumanReadableClassifier(curArgNum):
		variables["machineReadable"] = False
		return curArgNum

	def setMachineReadableClassifier(curArgNum):
		variables["machineReadable"] = True
		return curArgNum

	def setTestInputFile(curArgNum):
		curArgNum += 1
		variables["testInputFile"] = sys.argv[curArgNum]
		return curArgNum

	commandMapping = {"-training_input_file": setTrainingInputFile,
		"-human_readable_classifier": setHumanReadableClassifier,
		"-machine_readable_classifier": setMachineReadableClassifier,
		"-test_input_file": setTestInputFile}

	" Loop over the command arguments, setting fields in the variables dictionary." 
	curArgNum = 1
	while (curArgNum < len(sys.argv)):
		if sys.argv[curArgNum] in commandMapping:
			curArgNum = commandMapping[sys.argv[curArgNum]](curArgNum)
			curArgNum +=1

		else:
			print "Invalid command format."
			print "Valid options are -training_input_file, -human_readable_classifier, "
			print " -machine_readable_classifier, and -test_input_file"
			sys.exit(0)

	print "Training Input Filename :", variables["trainingInputFile"]
	print "Test Input Filename :", variables["testInputFile"]
	print "MachineReadable? :", variables["machineReadable"]
		

def learn():
	"""
	Learn should take in a filepath to the training data (given to main
	by the flag training_input_file) and return an object which can	classify 
	new data (which will be written to human_readable_classifier and
	machine_readable_classifier by main).
	"""


def classify():
	"""
	Classify should take in a classification object and a filepath to the
	testing data (given to main by machine_readable_classifier and test_input_file 
	respectively) and output a string of the line numbers in the testing which 
	evaluate to true (this will be written to a file specified by classify_results_file by main).
	"""



if __name__=='__main__':
	main(sys.argv)
