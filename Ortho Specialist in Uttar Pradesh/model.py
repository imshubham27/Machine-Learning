import pandas as pd

dataset = pd.read_csv('Processed_Dataset.csv')
X = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:,[4,5,6,7,8,9,10] ].values
print(X)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 1] = labelencoder.fit_transform(X[:, 1])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()

X = X[:, 1:]

"""from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 4/18, random_state = 0)"""

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_sca= sc_X.fit_transform(X)
sc_y = StandardScaler()
y_sca = sc_y.fit_transform(y)


# Multiple Linear Regression
from sklearn.linear_model import LinearRegression
mul_reg = LinearRegression()
mul_reg.fit(X_sca, y_sca)
y_pred_mul = mul_reg.predict(X_sca)

# Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)
y_pred_poly=lin_reg_2.predict(poly_reg.fit_transform(X))

#RandomForest Regression
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 280, random_state = 0)
regressor.fit(X, y)
y_pred_ran=regressor.predict(X)

#SVR
#

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)
y_pred_dt = regressor.predict(X)

# Multiple Linear Regression
from sklearn.metrics import r2_score
a1="Model accuracy of Multiple Linear Regression: "
b1=(r2_score(y_sca,y_pred_mul)*100)
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

print(lines)


txt_file=open('Model_accuracy.txt','w')
txt_file.writelines(lines)
txt_file.close()


