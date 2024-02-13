import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os

data = pd.read_csv("diabetes.csv")

# Feature Selection
x = data.drop(['Outcome'], axis=1)
y = data['Outcome']

from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(x,y, test_size=0.3, random_state=1)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

LRmodel = LogisticRegression()
DTmodel = DecisionTreeClassifier()
SVMmodel = svm.SVC(kernel = 'rbf')
RFmodel = RandomForestClassifier()
knnmodel = KNeighborsClassifier()

stTime = time.time()
osSttime = os.times()
LRmodel.fit(xTrain, yTrain)
DTmodel.fit(xTrain, yTrain)
SVMmodel.fit(xTrain, yTrain)
RFmodel.fit(xTrain, yTrain)
knnmodel.fit(xTrain, yTrain)
endTime = time.time()
osEndtime = os.times()

UserTime = osEndtime.user - osSttime.user
totalTime = endTime - stTime

yPredLR = LRmodel.predict(xTest)
yPredDT = DTmodel.predict(xTest)
yPredsvm = SVMmodel.predict(xTest)
yPredRF = RFmodel.predict(xTest)
yPredKnn = knnmodel.predict(xTest)

from sklearn.metrics import accuracy_score

logisticRegAccuracyScore = accuracy_score(yTest, yPredLR)*100
print("Logistic Regression Accuracy: ", logisticRegAccuracyScore)
DTAccuracyScore = accuracy_score(yTest, yPredDT)*100
print("Decision Tree Accuracy: ", DTAccuracyScore)
svmAccuracyScore = accuracy_score(yTest, yPredsvm)*100
print("SVM Accuracy: ", svmAccuracyScore)
RFAccuracyScore = accuracy_score(yTest, yPredRF)*100
print("Random Forest Accuracy: ", RFAccuracyScore)
KnnAccuracyScore = accuracy_score(yTest, yPredKnn)*100
print("KNN Accuracy: ", KnnAccuracyScore)

print(f"User CPU Time: {UserTime}")
print(f"System CPU Time: {totalTime}")