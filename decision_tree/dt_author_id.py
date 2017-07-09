#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

print "number of features:  ", len(features_train[0])

t0 = time()
print("training...")
clf = DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train, labels_train)
print "training time: " , time()-t0 , "s"

t0 = time()
print("predicting...")
pred = clf.predict(features_test)
print "prediction time: " , time()-t0 , "s"


print "accuracy score: ", accuracy_score(labels_test, pred)



#########################################################


