;from __future__ import print_function
import math
import sys
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset
import feature as f
from sklearn.metrics import r2_score

predict_dataframe = pd.read_csv("prediction.csv", sep=",")
predict_examples = f.preprocess_features(predict_dataframe)
predict_targets = f.preprocess_targets(predict_dataframe)

def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):

    # Convert pandas data into a dict of np arrays.
    features = {key:np.array(value) for key,value in dict(features).items()}

    # Construct a dataset, and configure batching/repeating.
    ds = Dataset.from_tensor_slices((features,targets)) # warning: 2GB limit
    ds = ds.batch(batch_size).repeat(num_epochs)

    # Shuffle the data, if specified.
    if shuffle:
      ds = ds.shuffle(10000)

    # Return the next batch of data.
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels

def construct_feature_columns(input_features):
    """Construct the TensorFlow Feature Columns.

    Args:
    input_features: The names of the numerical input features to use.
    Returns:
    A set of feature columns
    """
    return set([tf.feature_column.numeric_column(my_feature) for my_feature in input_features])

def train_model(
    learning_rate,
    steps,
    batch_size,
    training_examples,
    training_targets,
    validation_examples,
    validation_targets):

    periods = 15
    steps_per_period = steps / periods

    # Create a linear regressor object.
    my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
    linear_regressor = tf.estimator.LinearRegressor(feature_columns=construct_feature_columns(training_examples),optimizer=my_optimizer)

    # Create input functions.
    training_input_fn = lambda: my_input_fn(
        features=training_examples,
        targets=training_targets["actualTravelTimeSeconds"],
        batch_size=batch_size)
    predict_training_input_fn = lambda: my_input_fn(
        features=training_examples,
        targets=training_targets["actualTravelTimeSeconds"],
        num_epochs=1,
        shuffle=False)
    predict_validation_input_fn = lambda: my_input_fn(
        features=validation_examples,
        targets=validation_targets["actualTravelTimeSeconds"],
        num_epochs=1,
        shuffle=False)
    predict_input_fn = lambda: my_input_fn(
        features=predict_examples,
        targets=predict_targets["actualTravelTimeSeconds"],
        num_epochs=1,
        shuffle=False)

    # Train the model, but do so inside a loop so that we can periodically assess
    # loss metrics.
    print("Training model...")
    print("RMSE (on training data):")
    #file = open('training_output.txt', 'w')
    #sys.stdout = file
    training_rmse = []
    validation_rmse = []
    for period in range (0, periods):
        # Train the model, starting from the prior state.
        linear_regressor.train(
            input_fn=training_input_fn,
            steps=steps_per_period)

        # Take a break and compute predictions.
        training_predictions = linear_regressor.predict(input_fn=predict_training_input_fn)
        training_predictions = np.array([item['predictions'][0] for item in training_predictions])

        validation_predictions = linear_regressor.predict(input_fn=predict_validation_input_fn)
        validation_predictions = np.array([item['predictions'][0] for item in validation_predictions])

        predictions = linear_regressor.predict(input_fn=predict_input_fn)
        predictions = np.array([item['predictions'][0] for item in predictions])

        #Compute training and validation loss.
        training_root_mean_squared_error = math.sqrt(
        metrics.mean_squared_error(training_predictions, training_targets))
        validation_root_mean_squared_error = math.sqrt(
        metrics.mean_squared_error(validation_predictions, validation_targets))

        # R2 = r2_score(training_targets, training_predictions)
        # print("The R-Squared value is:", R2)
        # Occasionally print the current loss.
        print("  period %02d : %0.2f" % (period, training_root_mean_squared_error))
        if period == periods - 1:
            print("The predicted value is:")
            print(*predictions, sep = ", ")
            R2 = r2_score(validation_targets, validation_predictions)
            print("The R-Squared value is:", R2)
        # Add the loss metrics from this period to our list.
        training_rmse.append(training_root_mean_squared_error)
        validation_rmse.append(validation_root_mean_squared_error)
    print("Model training finished.")
    #file.close()

    # Output a graph of loss metrics over periods.
    plt.ylabel("RMSE")
    plt.xlabel("Periods")
    plt.title("Root Mean Squared Error vs. Periods")
    plt.tight_layout()
    plt.plot(training_rmse, label="training")
    plt.plot(validation_rmse, label="validation")
    plt.legend()
    plt.savefig('rmse_figure.png')
    plt.show(block=True)

    # Output a graph of loss metrics over periods.
    plt.ylabel("Predicted Value")
    plt.xlabel("Actual Value")
    plt.title("Actual Value vs. Predicted Value")
    plt.tight_layout()
    plt.xlim(0,200)
    plt.ylim(0, 200)
    plt.scatter(validation_targets, validation_predictions)
    plt.savefig('prediction_fig.png')
    plt.show(block=True)

    return linear_regressor

linear_regressor = train_model(
    learning_rate=0.00003,
    steps=500,
    batch_size=5,
    training_examples=f.training_examples,
    training_targets=f.training_targets,
    validation_examples=f.validation_examples,
    validation_targets=f.validation_targets
    )
