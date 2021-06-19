# Date 15-05-2021
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets as dt, linear_model as lm
from sklearn.metrics import mean_squared_error as mse
# sklearn.metrics.mean_squared_error

diabetes = dt.load_diabetes()
# print(diabetes)
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])
# print(diabetes.keys())
# print(np.size(diabetes.data))
# print(diabetes.data)
# print(diabetes.DESCR)
diabetes_x = diabetes.data[:, np.newaxis, 2]
diabetes_x_train = diabetes_x[:-400]
diabetes_x_test = diabetes_x[-30:]

# diabetes_y = diabetes.target[:, np.newaxis, 2]
diabetes_y_train = diabetes.target[:-400]
diabetes_y_test = diabetes.target[-30:]

model = lm.LinearRegression()
model.fit(diabetes_x_train, diabetes_x_train)
# model.fit(diabetes_x_test, diabetes_y_test)
diabetes_y_predicted = model.predict(diabetes_x_test)

print('Mean Squared Error is:', mse(diabetes_y_test, diabetes_y_predicted))

print('Weights is:', model.coef_)
print('Intercept is:', model.intercept_)

# print(diabetes_x)
# print(diabetes_x_train)
# print(diabetes_x_test)


plt.scatter(diabetes_x_test, diabetes_y_test)
plt.plot(diabetes_x_test, diabetes_y_predicted)
plt.show()
