# Linear Regression

import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error

diabetes=datasets.load_diabetes()
diabetes_X=diabetes.data
# (['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])

diabetes_X_train=diabetes_X[:-30]
diabetes_X_test=diabetes_X[-30:]

diabetes_Y_train=diabetes.target[:-30]
diabetes_Y_test=diabetes.target[-30:]

model=linear_model.LinearRegression()
model.fit(diabetes_X_train,diabetes_Y_train)

Y_predict=model.predict(diabetes_X_test)
print("MSE: ",mean_squared_error(diabetes_Y_test,Y_predict))
print("slope: "+str(model.coef_))
print("intercept: "+str(model.intercept_))

# plt.scatter(diabetes_X_test,diabetes_Y_test)
# plt.plot(diabetes_X_test,Y_predict)

# plt.show()


