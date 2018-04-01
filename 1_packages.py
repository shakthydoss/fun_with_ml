# This tutorial is about understanding scikit packages for machine learning.

# By default scikit comes with preloaded data set for practicing machine leaning algorithms.
from sklearn import datasets

# In sklean package algorithms are group into package based on the way it works.

# from sklearn.naive_bayes 
# This module has implementation for all algorithms that work based on naive bayes module 
# Popular algorithms in this package. 
from sklearn.naive_bayes import BernoulliNB     
from sklearn.naive_bayes import MultinomialNB   

# from sklearn.neighbors
# This module has implementation for k-nearest neighbors algorithms
from sklearn.neighbors import KNeighborsClassifier # Classfication based KNN
from sklearn.neighbors import KNeighborsRegressor # Regression based KNN 
from sklearn.neighbors import NearestNeighbors # Classfication  
from sklearn.neighbors import NearestCentroid # Nearest centroid classifier

# from sklearn.linear_model
# This module has implementation for all algorithms that work based on generalized linear modules
# Popular algorithms in this packages.
from sklearn.linear_model import LinearRegression     # Regression  
from sklearn.linear_model import LogisticRegression   # Classification 

# from sklean.svm 
# This module has implementation for SVM based algorithm.
# Pouplar algorithms in this packages. 
from sklearn.svm import LinearSVC  # Linear support vector for Classification 
from sklearn.svm import LinearSVR  # Linear support vector for Regression 
from sklearn.svm import SVC        # C support vector Classification
from sklearn.svm import SVR        # Epsilon support vector Regression

# from sklean.clustering
# This module gathers most popular clustering algorithms 
# popular algorithms in this packages. 
from sklearn.cluster import KMeans 


# from sklearn.metrics 
# Has functions for measuring performance of various algorithm  
# popular Classification metrics
from sklearn.metrics import accuracy_score 
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from sklearn.metrics import f1_score
from sklearn.metrics import jaccard_similarity_score
# popular Regression metrics 
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score