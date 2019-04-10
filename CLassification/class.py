import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Logistic Regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

y_pred_log = classifier.predict(X_test)

from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_log))

#K Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)

y_pred_knn = classifier.predict(X_test)

from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_knn))

#Kernel Support Vector Machine
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(X_train, y_train)

y_pred_svm = classifier.predict(X_test)

from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_svm))

#Naive Bayes
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred_nb = classifier.predict(X_test)

from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_nb))

#Decision Tree
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

y_pred_dt = classifier.predict(X_test)

from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_dt))

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

y_pred_rf = classifier.predict(X_test)

from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_rf))