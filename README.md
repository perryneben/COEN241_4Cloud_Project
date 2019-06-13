# COEN241_4Cloud_Project
Team 4Cloud Project

ML Local Training Instructions

The easiest way to run the ML training programs is to install Anaconda. It comes with Scikit-Learn
and pandas libaries and a ready-make environment to run the scripts.

https://www.anaconda.com/distribution/

The primary non-Python-standard libraries are:

https://pandas.pydata.org/   
https://scikit-learn.org/stable/

Generating simulated data example:

	python generateTrainingData newData.csv 5000

5000 new data samples will be written to newData.csv.

Machine Learning survey of different regression algorithms:

	python machineLearningTrain.py training_samples_10k.csv
	
This will use 10k samples to train various regression algorithms and provie R-Squared values for each.

Use a trained model to predict a value:

	python predictML.py
	
This will automatically use the training_samples_10k.csv.

After having completed the above one needs to ensure the terminal is in the coen241_4cloud_project folder.  Once in this folder, to run the simulator, one needs to type "python simulator.py".
Once the simulator is started, a user needs to input a start and end node on the city map.  The rows available are from A to L and the columns are from 0 to 8.  An example is a start point of A0 to L8.  These are two far edges on the city map.
