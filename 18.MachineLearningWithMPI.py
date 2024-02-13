from mpi4py import MPI
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# Get the rank of the process and the size of the communicator
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

data = pd.read_csv("diabetes.csv")

# Feature Selection
x = data.drop(['Outcome'], axis=1)
y = data['Outcome']

from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(x,y, test_size=0.3, random_state=1)


if rank == 0:
    LRmodel = LogisticRegression()

    stTime = time.time()
    osSttime = os.times()
    LRmodel.fit(xTrain, yTrain)
    endTime = time.time()
    osEndtime = os.times()
    UserTime = osEndtime.user - osSttime.user
    totalTime = endTime - stTime

    yPredLR = LRmodel.predict(xTest)

    logisticRegAccuracyScore = accuracy_score(yTest, yPredLR)*100
    print("Logistic Regression Accuracy: ", logisticRegAccuracyScore)

    print(f"User CPU Time: {UserTime}")
    print(f"System CPU Time: {totalTime}")

if rank == 1:
    DTmodel = DecisionTreeClassifier()

    stTime = time.time()
    osSttime = os.times()
    DTmodel.fit(xTrain, yTrain)
    endTime = time.time()
    osEndtime = os.times()
    UserTime = osEndtime.user - osSttime.user
    totalTime = endTime - stTime

    yPredDT = DTmodel.predict(xTest)

    DTAccuracyScore = accuracy_score(yTest, yPredDT)*100
    print("Decision Tree Accuracy: ", DTAccuracyScore)

    print(f"User CPU Time: {UserTime}")
    print(f"System CPU Time: {totalTime}")

if rank == 2:
    SVMmodel = svm.SVC(kernel = 'rbf')

    stTime = time.time()
    osSttime = os.times()
    SVMmodel.fit(xTrain, yTrain)
    endTime = time.time()
    osEndtime = os.times()
    UserTime = osEndtime.user - osSttime.user
    totalTime = endTime - stTime

    yPredsvm = SVMmodel.predict(xTest)

    svmAccuracyScore = accuracy_score(yTest, yPredsvm)*100
    print("SVM Accuracy: ", svmAccuracyScore)

    print(f"User CPU Time: {UserTime}")
    print(f"System CPU Time: {totalTime}")


if rank == 3:
    RFmodel = RandomForestClassifier()

    stTime = time.time()
    osSttime = os.times()
    RFmodel.fit(xTrain, yTrain)
    endTime = time.time()
    osEndtime = os.times()
    UserTime = osEndtime.user - osSttime.user
    totalTime = endTime - stTime

    yPredRF = RFmodel.predict(xTest)

    RFAccuracyScore = accuracy_score(yTest, yPredRF)*100
    print("Random Forest Accuracy: ", RFAccuracyScore)

    print(f"User CPU Time: {UserTime}")
    print(f"System CPU Time: {totalTime}")

if rank == 4:
    knnmodel = KNeighborsClassifier()

    stTime = time.time()
    osSttime = os.times()
    knnmodel.fit(xTrain, yTrain)
    endTime = time.time()
    osEndtime = os.times()
    UserTime = osEndtime.user - osSttime.user
    totalTime = endTime - stTime

    yPredKnn = knnmodel.predict(xTest)

    KnnAccuracyScore = accuracy_score(yTest, yPredKnn)*100
    print("KNN Accuracy: ", KnnAccuracyScore)

    print(f"User CPU Time: {UserTime}")
    print(f"System CPU Time: {totalTime}")