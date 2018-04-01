# This tutorial is more about understanding datasets in scikit 

# Toy Dataset
# By default scikit comes with preloaded data set for practicing machine leaning algorithms.
from sklearn import datasets
iris_data      = datasets.load_iris() # Classification 
wine_data      = datasets.load_wine() # Classification 
cancer_data    = datasets.load_breast_cancer() # Classification
diabetes_data  = datasets.load_diabetes() # Regression 
boston_data    = datasets.load_boston() # Regression 
linnerud_data  = datasets.load_linnerud() # Multivariate Regression

# Accessing data
# By default datasets return Bunch - Dictionary like object. 
# Bunch has target variable (Y) and feature variable (X). 
X = iris_data.get("data")
Y = iris_data.get("target")
feature_names = iris_data.get("feature_names")
target_names = iris_data.get("target_names") # nothing but lable name 

X = diabetes_data.get("data")
Y = diabetes_data.get("target")
feature_names = diabetes_data.get("feature_names")
# for regression problems there is no target_names


# for more details about dataset visit 
# http://scikit-learn.org/stable/datasets/index.html#datasets
