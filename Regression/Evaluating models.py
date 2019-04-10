# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:59:09 2019

@author: shubh
"""
# Simple Linear Regression
from sklearn.metrics import r2_score
a1="Model accuracy of Simple Linear Regression: "
b1=(r2_score(y,y_pred_sim)*100)
c1='{}{}{}'.format(a1,b1,'% \n')

# Polynomial Regression
from sklearn.metrics import r2_score
a2="Model accuracy of Polynomial Regression: "
b2=(r2_score(y,y_pred_poly)*100)
c2='{}{}{}'.format(a2,b2,'% \n')

# RandomForest Regression
from sklearn.metrics import r2_score
a3="Model accuracy of Random Forest Regression: "
b3=(r2_score(y,y_pred_ran)*100)
c3='{}{}{}'.format(a3,b3,'% \n')

# DecisionTree Regression
from sklearn.metrics import r2_score
a4="Model accuracy of Decision Tree Regression: "
b4=(r2_score(y,y_pred_dec)*100)
c4='{}{}{}'.format(a4,b4,'% \n')

#SVR
from sklearn.metrics import r2_score
a5="Model accuracy of Support Vector Regression: "
b5=(r2_score(y,y_pred_svr)*100)
c5='{}{}{}'.format(a5,b5,'% \n')

lines=[c1,c2,c3,c4,c5]

txt_file=open('Model_accuracy.txt','w')
txt_file.writelines(lines)
txt_file.close()
