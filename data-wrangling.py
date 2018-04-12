import pandas as pd 
data = pd.read_csv("iris_data.csv")
print data.columns
#print data.values
# print data.index

# print data.sort_values(by=["sepal_width", "petal_width"], ascending=[True, True])
# print data.loc[0:3,["sepal_length", "sepal_width"]]
# print data.shape
# print data.ndim

print data.describe()
print data.sum(1)