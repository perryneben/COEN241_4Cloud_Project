#!/bin/python

import trainingData
import sys
import pandas
from sklearn.linear_model import BayesianRidge

names = trainingData.getNames()
dataset = pandas.read_csv('training_samples_10k.csv', names=names)
array = dataset.values
X = array[:,0:16]
Y = array[:,16]
brmodel = BayesianRidge()
brmodel.fit(X, Y)

# The following function expects an array of the 16 variables required to
# predict the travel time with the ML model.
#
# Variable names in order:
#
# ['lengthFeet', 'speedLimitMph', 'numLanes', 'dividedTraffic', 'trafficLights',
#  'stopSigns', 'pedestrianCrossings', 'dayOfWeek', 'holiday', 'timeOfDay', 'cloudWeather',
#  'cloudTraffic', 'cloudEvent', 'localWeather', 'localTraffic', 'localEvent', 'travelTimeSeconds']
#
# Example set of variables:
#
# exampleVars = [600, 15, 3, 1, 0, 1, 1, 5, 1, 1000, 1, 2, 0, 1, 2, 0]
#
def predict(variables):
    vars = [variables]
    return brmodel.predict(vars)

# Example code prdicting the travel time.

exampleVars = [600, 15, 3, 1, 0, 1, 1, 5, 1, 1000, 1, 2, 0, 1, 2, 0]
trainingData.printVars(exampleVars)
predictedTime = predict(exampleVars)
print("\nPredicted time: %d" % predictedTime)