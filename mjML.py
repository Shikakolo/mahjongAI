# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 11:24:56 2018

@author: p_giacominsanou
"""
 
#Learning machines:
#from sklearn.naive_bayes import MultinomialNB #For my own entretainment
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Perceptron 
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import f1_score
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.feature_extraction.text import TfidfTransformer
#from sklearn.pipeline import Pipeline
#from sklearn.model_selection import GridSearchCV 
 
#Metric tools
from sklearn.metrics import classification_report

#useful libs
import os
import pandas as pd
import numpy as np
from sklearn.externals import joblib

#should be a float number 0 < trian_ratio < 1
train_ratio = 0.7
count = 0
directories = os.fsencode("./csvs/")
directory_length=  len(os.listdir(directories))
train_amount = int(directory_length * train_ratio)
test_amount = directory_length - train_amount

svm = SVC(kernel='rbf', gamma="auto")

for directory in os.listdir(directories):
    
    if count > (train_value):
        break
    
    dirname = directories + os.fsencode(directory + b"/")
    count += 1

    for file_ in os.listdir(dirname):
        if file_.endswith(b".csv"):
            filename_str = (dirname + file_).decode('utf-8')
            file = open(filename_str, "r", encoding = "utf-8")
            file = file.read()
            columns = [i for i in range(20 + 1)]
            df = pd.read_csv(filename_str, delimiter=',', header= None, names = columns, engine = 'python', skipfooter = 1)
            df = df.fillna(value=int(-1))
            if(len(df) < 2):
                continue
            y_labels = df.iloc[:, 0]
            X_ = df.iloc[:, 1:]
            
            svm.fit(X_, y_labels)
            
joblib.dump(svm, "SVM-rbf.joblib", compress=True)
"""

svm = joblib.load("SVM-rbf.joblib")
f1_scores = []

for i in range(test_amount):

    directory = os.listdir(directories)[train_amount + i]
    dirname = directories + os.fsencode(directory + b"/")
    count += 1

    for file_ in os.listdir(dirname):
        if file_.endswith(b".csv"):
            filename_str = (dirname + file_).decode('utf-8')
            
            file = open(filename_str, "r", encoding = "utf-8")
            file = file.read()
            columns = [i for i in range(20 + 1)]
            df = pd.read_csv(filename_str, delimiter=',', header= None, names = columns, engine = 'python', skipfooter = 1)
            df = df.fillna(value=int(-1))

            y_labels = df.iloc[:, 0]
            X_ = df.iloc[:, 1:]
            prediction = svm.predict(X_)
            f1_scores.append(f1_score(y_labels, prediction, average = 'micro')*100)
            #print( "a file has been tested!")

print(f1_scores)
            """
    
            
      

