from sklearn import datasets

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error


import numpy as np
import pandas as pd


# from sklearn import datasets
# from sklearn.linear_model import LogisticRegression
# from sklearn import metrics

iris_data = datasets.load_iris()
X = iris_data.data
Y = iris_data.target

logReg = LogisticRegression()

logReg.fit(X, Y)
#Yhat = logReg.predict(X)

#
# from sklearn import metrics
#
# print metrics.accuracy_score(Y, Yhat)
#
# from sklearn.neighbors import KNeighborsClassifier
#
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X, Y)
# Yhat = knn.predict(X)
#
# print metrics.accuracy_score(Y, Yhat)
#
# knn = KNeighborsClassifier(n_neighbors=1)
# knn.fit(X, Y)
# Yhat = knn.predict(X)
#
# print metrics.accuracy_score(Y, Yhat)
#
from sklearn.model_selection import train_test_split
#
# x_tain, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=4)
#
# print x_tain.shape
# print x_test.shape
#
# k_range = range(1,25)
# score = list()
# for k in k_range:
#     knn = KNeighborsClassifier(n_neighbors=k)
#     knn.fit(x_tain,y_train)
#     Yhat = knn.predict(x_test)
#     score.append(metrics.accuracy_score(y_test, Yhat))
#
# print score

import matplotlib.pyplot as plt
# plt.plot(k_range, score)
# plt.xlabel("K value.")
# plt.ylabel("Accuracy score.")
# plt.show()

import pandas as pd

data = pd.read_csv("http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv", index_col=0)

x = data[["TV", "radio", "newspaper"]]
y = data["sales"]

x_tain, x_test, y_tain, y_test = train_test_split(x, y)

print x_tain.shape
print y_tain.shape
print x_test.shape
print y_test.shape
from sklearn.linear_model import LinearRegression

linreg = LinearRegression()

linreg.fit(x_tain, y_tain)

yhat = linreg.predict(x_tain)

import numpy as np
print np.sqrt(metrics.mean_squared_error(y_tain, yhat))