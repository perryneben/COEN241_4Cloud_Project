from __future__ import print_function
from IPython import display
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 20
pd.options.display.float_format = '{:.1f}'.format

traffic_dataframe = pd.read_csv("newTraining_20k.csv", sep=",")
traffic_dataframe = traffic_dataframe.reindex(
     np.random.permutation(traffic_dataframe.index))
size = traffic_dataframe.size

def preprocess_features(traffic_dataframe):
  """Prepares input features from traffic data set.

  Args:
    traffic_dataframe: A Pandas DataFrame expected to contain data
      from the traffic data set.
  Returns:
    A DataFrame that contains the features to be used for the model
  """
  #lengthFeet, speedLimit,numLanes, dividedTraffic, trafficLights, stopSigns,
  #pedCrossings, dayOfWeek, holiday,timeOfDayMinutes, cloudWeather, cloudTraffic,
  #cloudEvent, localWeather, localTraffic,localEvent, actualTravelTimeSeconds
  processed_features = traffic_dataframe[
    ["lengthFeet",
     "speedLimit",
     "numLanes",
     "dividedTraffic",
     "trafficLights",
     "stopSigns",
     "pedCrossings",
     "dayOfWeek",
     "holiday",
     "timeOfDayMinutes",
     "cloudWeather",
     "cloudTraffic",
     "cloudEvent",
     "localWeather",
     "localTraffic",
     "localEvent"
     ]]
  #processed_features = selected_features.copy()
  return processed_features

def preprocess_targets(traffic_dataframe):
  """Prepares target features (i.e., labels) from traffic data set.
  Args:
    traffic_dataframe: A Pandas DataFrame expected to contain data
      from the traffic data set.
  Returns:
    A DataFrame that contains the target feature.
  """
  output_targets = pd.DataFrame()
  output_targets["actualTravelTimeSeconds"] = traffic_dataframe["actualTravelTimeSeconds"]
  return output_targets

training_examples = preprocess_features(traffic_dataframe.head((int)(size * 0.8)))
training_examples.describe().to_csv("training_examples.csv")
print(training_examples.describe())

training_targets = preprocess_targets(traffic_dataframe.head((int)(size * 0.8)))
training_targets.describe().to_csv("training_targets.csv")
print(training_targets.describe())

validation_examples = preprocess_features(traffic_dataframe.tail((int)(size * 0.2)))
validation_examples.describe().to_csv("validation_examples.csv")
print(validation_examples.describe())

validation_targets = preprocess_targets(traffic_dataframe.tail((int)(size * 0.2)))
validation_targets.describe().to_csv("validation_targets.csv")
print(validation_targets.describe())
