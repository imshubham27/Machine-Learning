# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:51:04 2019

@author: shubh
"""

#Visualising Simple Linear Regression
plt.scatter(X, y, color = 'red')
plt.plot(X, y_pred_sim, color = 'blue')
plt.title('Salary vs Position Level(Simple Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#Visualising  Polynomial Regression
plt.scatter(X, y, color = 'red')
plt.plot(X, y_pred_poly, color = 'blue')
plt.title('Salary vs Position Level(Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


#Visualising  RandomForest Regression
plt.scatter(X, y, color = 'red')
plt.plot(X, y_pred_ran, color = 'blue')
plt.title('Salary vs Position Level(RandomForest Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#Visualising  DecisionTree Regression
plt.scatter(X, y, color = 'red')
plt.plot(X, y_pred_dec, color = 'blue')
plt.title('Salary vs Position Level(DecisionTree Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#Visualising SVR
plt.scatter(X, y, color = 'red')
plt.plot(X, y_pred_svr, color = 'blue')
plt.title('Salary vs Position Level(SVR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()