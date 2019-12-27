
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


lines=[c1,c2,c3]


txt_file=open('Model_accuracy.txt','w')
txt_file.writelines(lines)
txt_file.close()
