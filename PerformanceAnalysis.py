import sys
"""
Author: Kevin Zeillmann
"""
def main(args):
	#start by processing our answer key
	answerKey = processKnownData("WisconsinBreastCancerDatasets.csv")
	#then get our results
	results = processResults("outputFile.txt")
		
	#next calculate number correct
	numRight = 0
	correctPositive = 0 #correctly predicted value of true
	correctNegative = 0 #correctly predicted value of false
	falsePositive = 0 #incorrectly predicted value of true
	falseNegative = 0 #incorrectly predicted value of false
	
	for key in answerKey:
		
		if answerKey[key] == "TRUE" and key in results:
			correctPositive += 1
		elif answerKey[key] == "TRUE" and key not in results:
			falseNegative += 1
		elif answerKey[key] == "FALSE" and key not in results:
			correctNegative +=1
		elif answerKey[key] == "FALSE" and key in results:
			falsePositive +=1
			
			
	numRight = correctPositive + correctNegative
	print "Percent correct: " + str(100*numRight/float(len(answerKey)))


def processKnownData(filename):
	"""
	This function parses through the CSV file to find the actual true/false values
	in the training data. 
	"""
	
	trueFalseDict = dict()
	data = open(filename, 'r')
	nextLine = data.readline()
	rowNum = 1
	while nextLine:
		
		if "TRUE" in nextLine:
			trueFalseDict[rowNum] = "TRUE"
		else:
			trueFalseDict[rowNum] = "FALSE"
		nextLine = data.readline()	
		rowNum += 1
		
	return trueFalseDict
	
def processResults(filename):
	trueSet = set()
	resultData = open(filename, 'r')
	nextLine = resultData.readline()
	while nextLine:
		trueSet.add(int(nextLine)+1)
		nextLine = resultData.readline()
	return trueSet
	

if __name__=='__main__':
	main(sys.argv)