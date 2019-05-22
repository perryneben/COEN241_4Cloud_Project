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

models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)