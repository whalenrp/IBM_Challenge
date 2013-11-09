IBM Challenge
=============

This folder contains the python scripts necessary to learn from and classify
a csv training file with continuously valued variables. We implemented two
different learners, a bagging learner and a decision tree learner. To do this
we created an "abstract" base class in AbstractLearner.py that contains all the
file input parsing and processing. Derived classes, BaggingLearner and SimpleLearner
can then simply chain to the base class constructor and access the data stored there
after construction. 

TestCrossValidator.bat is a batch file which tests PerformanceAnalysis.py which 
determines the accuracy of our algorithm. It examines the WisconsinBreastCancerDataSets.csv
file and compares it to the output of outputFile.txt to determine accuracy. 

WisconsinBreastCancerTest.csv is the same as WisconsinBreastCancerDatasets.csv, except with the
truth values removed. This allows us to test the accuracy of the dataset on itself. 
We train on the data, and then we test on the same data. This is done in TestWisconsin.bat. 

Our divion of labor is as follows:
Kevin Flanagan  : Bagging classification, SimpleLearner, Project writeup
Kevin Zeillmann : Output processing, analysis, and automation and performance tuning for accuracy
Richard Whalen  : Project architecture, IO and data sanitization, 
					DecisionTree creation, Bagging Forest creation
