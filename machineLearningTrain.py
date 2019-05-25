#!/bin/python

import trainingData
import sys
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import LassoLars
from sklearn.linear_model import MultiTaskLasso
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import MultiTaskElasticNet
from sklearn.linear_model import OrthogonalMatchingPursuit
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import ARDRegression
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import SGDRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
if len(sys.argv) < 2:
    print("Must provide csv file of training data")
    sys.exit(1)
    
csvPath = sys.argv[1]

names = []
for variable in trainingData.trainingDataDefinition:
    names.append(variable['name'])
    
print(names)

dataset = pandas.read_csv(csvPath, names=names)

# Some code to look at the training data. 
print(dataset.shape)
#print(dataset.head(20))
#print(dataset.describe())
#scatter_matrix(dataset)
#plt.show()

array = dataset.values
print(array)
#sys.exit(0)
X = array[:,0:16]
Y = array[:,16]
validation_size = 0.20
seed = 7
scoring = 'explained_variance'
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

print(X_train.shape)
print(Y_train.shape)
print(X_validation.shape)
print(Y_validation.shape)

models = []
models.append(('LinearRegression', LinearRegression())) # r^2 of 0.774
models.append(('Lasso', Lasso(alpha=0.1))) # r^2 of 0.773
models.append(('LassoLars', LassoLars(alpha=0.01))) # r^2 of 0.773
models.append(('ElasticNet', ElasticNet(random_state=0, alpha=0.1))) # r^2 of 0.727
models.append(('OrthogonalMatchingPursuit', OrthogonalMatchingPursuit())) # r^2 of 0.349
models.append(('BayesianRidge', BayesianRidge())) # r^2 of 0.774
models.append(('KernelRidge', KernelRidge(alpha=1.0))) #r^2 of 0.754
# models.append(('ARDRegression', ARDRegression())) # r^2 of ??? Doesn't complete.
#models.append(('SVR', SVR(gamma='auto'))) # r^2 of 0.005
#models.append(('SGDRegressor_sl', SGDRegressor(max_iter=1000, tol=1e-3, loss="squared_loss"))) # Doesn't work, negative r^2
models.append(('SGDRegressor_h', SGDRegressor(max_iter=1000, tol=1e-3, loss="huber"))) # r^2 of 0.388
#models.append(('SGDRegressor_ei', SGDRegressor(max_iter=1000, tol=1e-3, loss="epsilon_insensitive"))) # Doesn't work, negative r^2
#models.append(('GaussianProcessRegressor', GaussianProcessRegressor())) # r^2 of 0.003

results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s r^2: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
	print(cv_results)