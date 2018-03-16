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

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#counting number of persons in dataset
peopleCount = len(enron_data.keys())
print(peopleCount)

#counting number of features per person
peopleFeaturesCount = len(enron_data['METTS MARK'])
print(peopleFeaturesCount)

#counting POI's
pois = 0
for keys in enron_data:
    if(enron_data[keys]['poi'] == True):
        pois += 1
print(pois)

#how many pois exist
realPois = 0
namesFile = open('../final_project/poi_names.txt','r')
for line in namesFile:
    if('(y)' in line or '(n)' in line):
        realPois += 1
print(realPois)


