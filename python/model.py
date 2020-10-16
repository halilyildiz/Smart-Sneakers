# -*- coding: utf-8 -*-
"""
Created on Sat May 23 01:44:23 2020

@author: halil
"""

#%% libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
#%% read_csv

data = pd.read_csv("C:\\Users\halil\\Desktop\\Smart-Sneaker\\datas\\data.csv")

#%% x ve y olarak veriyi parçalama
x = data.iloc[:,:32]
y = data.iloc[:,-1]

#%% sınıfları 0 ve 1 lere çevirme

for each in range(len(y)):
    if y[each] =="downstairs":
        y[each] = 0
    elif y[each] =="upstairs":
        y[each] = 1
    elif y[each] =="walk":
        y[each] = 2
    elif y[each] =="run":
        y[each] = 3
   
#%% Verileri normalize etme
x_ = x
x = x = (x - np.min(x))/(np.max(x)-np.min(x))

#%%
y=y.astype('int')
#%% Veriyi eğiti ve test olarak parçalama
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 24)

#%% KNN Modeli
from sklearn.neighbors import KNeighborsClassifier
score_list = list()

knn = KNeighborsClassifier(n_neighbors = 6)
knn.fit(x_train,y_train)
score_list.append(knn.score(x_test,y_test))
knn_pred = knn.predict(x_test)
print("KNN score: ",knn.score(x_test,y_test))
print(classification_report(y_test, knn_pred)) 


#%% SVM Modeli
from sklearn.svm import SVC

svm = SVC(random_state=1)
svm.fit(x_train,y_train)

svmy_pred = svm.predict(x_test)
print("SVC score: ",svm.score(x_test,y_test))
print(classification_report(y_test, svmy_pred)) 

#%% Naive Bayes Modeli

from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(x_train,y_train)

nby_pred = nb.predict(x_test)
print("Naive-Bayes score: ",nb.score(x_test,y_test))
print(classification_report(y_test, nby_pred)) 
 
#%% Decission TreeModeli
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(x_train,y_train)

dsc_pred = dt.predict(x_test)

print("Decision Tree score: ", dt.score(x_test,y_test))
print(classification_report(y_test, dsc_pred)) 
#%% Random Forest Modeli
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators = 90,random_state = 1)
rf.fit(x_train,y_train)
print("Random Forest score: ",rf.score(x_test,y_test))

rfy_pred = rf.predict(x_test)
print(classification_report(y_test, rfy_pred)) 


#%% Confusion matrsi oluşturma
from sklearn.metrics import  confusion_matrix

cm = confusion_matrix(y_test,rfy_pred)

#%% visualization
"""
f, ax = plt.subplots(figsize = (5,5))
sns.heatmap(cm, annot = True, linewidth = 0.5, fmt = ".0f", ax=ax)
plt.xlabel("rfy_pred")  
plt.ylabel("y_test")    
plt.show()
"""

#%%
"""
score_list = []
for each in range(1,500):
    rf = RandomForestClassifier(n_estimators = each,random_state = 1)
    rf.fit(x_train,y_train)
    score_list.append(rf.score(x_test,y_test))
    """
#%% 

plt.plot(range(1,30),score_list)
plt.xlabel("n_estimators")
plt.ylabel("accuracy")
plt.show()
