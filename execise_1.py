from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression


# Toy dataset 
iris_data = datasets.load_iris()
boston_data = datasets.load_boston()
cancer_data = datasets.load_breast_cancer()
wine_data = datasets.load_wine()

X = iris_data.get("data")
data_feature_names = iris_data.get("feature_names")
Y = iris_data.get("target")
target_name = iris_data.get("target_names")


logReg = LogisticRegression()
logReg.fit(X, Y)
predicted_y = logReg.predict(X)
print predicted_y

from sklearn import metrics

print metrics.accuracy_score(predicted_y,Y)
