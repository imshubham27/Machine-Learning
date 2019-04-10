#Logistic Regression
from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_log))

#KNN
from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_knn))

#SVM
from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_svm))

#Naive Bayes
from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_nb))

#Decision Tree
from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_dt))

#Random Forest
from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_rf))