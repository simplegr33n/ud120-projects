#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop( "TOTAL", 0 ) 
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

# Find Max Salary
max_salary_1 = 0
max_salary_1_key = ''
for data_element in data_dict:
# print data_element[0]['salary']
    if data_dict[data_element]['salary'] != 'NaN' and data_dict[data_element]['salary'] > max_salary_1:
        max_salary_1 = data_dict[data_element]['salary']
        max_salary_1_key = data_element

print max_salary_1_key
print max_salary_1



