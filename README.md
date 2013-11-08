IBM Challenge
=============

This folder contains the python scripts necessary to learn from and classify
a csv training file with continuously valued variables. We implemented two
different learners, a bagging learner and a decision tree learner. To do this
we created an "abstract" base class in AbstractLearner.py that contains all the
file input parsing and processing. Derived classes, BaggingLearner and SimpleLearner
can then simply chain to the base class constructor and access the data stored there
after construction. 

Our divion of labor is as follows:
Kevin Flanagan  : Bagging classification, SimpleLearner, Project writeup
Kevin Zeillmann : Output processing, analysis, and automation and performance tuning for accuracy
Richard Whalen  : Project architecture, IO and data sanitization, 
					DecisionTree creation, Bagging Forest creation
