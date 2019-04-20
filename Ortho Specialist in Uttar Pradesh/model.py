import pandas as pd

dataset = pd.read_csv('Processed_Dataset.csv')
X = dataset.iloc[:, [1,5]].values
y = dataset.iloc[:,[2,3,6,7,8,9,10] ].values
print(X)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 0] = labelencoder.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

X = X[:, 1:]

"""from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 4/18, random_state = 0)"""

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_sca= sc_X.fit_transform(X)
sc_y = StandardScaler()
y_sca = sc_y.fit_transform(y)



# Simple Linear Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)
y_pred_sim = regressor.predict(X)

# Polynomial Regression
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

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



