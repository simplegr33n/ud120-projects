#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
from __future__ import division
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print all names
for key, value in enron_data.iteritems() :
    print key

# print sample value
print "\n======Example SKILLING JEFFERY K======"
print enron_data["SKILLING JEFFREY K"]
print "=======================================\n"

# quiz answers
number_of_people = len(enron_data)
print "number of people: ", len(enron_data)

print "number of features: ", len(enron_data["SKILLING JEFFREY K"])

sum_poi = 0
for x in enron_data:
    if enron_data[x]["poi"] == 1:
		sum_poi += 1

print "number of PoI: ", sum_poi

print "James Prentice total_stock_value: ", enron_data["PRENTICE JAMES"]['total_stock_value']

print "Wesley Colwell from_this_person_to_poi: ", enron_data["COLWELL WESLEY"]['from_this_person_to_poi']
 
print "Jeffrey Skilling  exercised_stock_options: ", enron_data["SKILLING JEFFREY K"]['exercised_stock_options']

print "Total Payments: Lay: %r, Skilling: %r, Fastow: %r" % (enron_data["LAY KENNETH L"]['total_payments'], enron_data["SKILLING JEFFREY K"]['total_payments'], enron_data["FASTOW ANDREW S"]['total_payments'])

quantified_salary = 0
for x in enron_data:
    if enron_data[x]["salary"] != "NaN":
		quantified_salary += 1
print "number with quantified salary: ", quantified_salary

email_known = 0
for x in enron_data:
    if enron_data[x]["email_address"] != "NaN":
		email_known += 1
print "number with known email: ", email_known

NaN_payments = 0
for x in enron_data:
    if enron_data[x]["total_payments"] == "NaN":
		NaN_payments += 1
		NaN_percentage = NaN_payments / number_of_people
print "number with unknown payments: ", NaN_percentage

NaN_payments_poi = 0
for x in enron_data:
    if enron_data[x]["poi"]:
        if enron_data[x]["total_payments"] == "NaN":
		   NaN_payments_poi += 1
		   NaN_payments_poi = NaN_payments_poi / number_of_people
print "number of poi with unknown payments: ", NaN_payments_poi

print "number of people + 10: ", number_of_people + 10

print "number of unknown payments + 10: ", NaN_payments + 10

print "POIs + 10: ", sum_poi + 10

print "POIs with NaN payments + 10: ", NaN_payments_poi + 10









