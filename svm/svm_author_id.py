#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

clf = svm.SVC(kernel='rbf',C=10000.0,gamma='auto')

# Reduce to 1% of data to speed up svm training and prediction
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 


# Train and time the train
t0 = time()
print "training..."
clf.fit(features_train, labels_train)
print "train time:", round(time()-t0, 3), "s"

# Predict and time prediction
t0 = time()
print "predicting..."
pred = clf.predict(features_test)
print "predict time:", round(time()-t0, 3), "s"

# Prediction at 10, 26, 50
print "10th: %r, 26th: %r, 50th: %r" % (pred[10], pred[26], pred[50])

# Number predicted to be Chris(1)
print "No. of predicted to be in the 'Chris'(1): %r" % sum(pred) #simply find sum, as Sara is (0)



from sklearn.metrics import accuracy_score
print "accuracy score: ", accuracy_score(labels_test, pred)



#########################################################


