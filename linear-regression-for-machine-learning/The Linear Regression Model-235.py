## 2. Introduction To The Data ##

import pandas as pd
data = pd.read_csv("AmesHousing.txt" , delimiter = "\t")
train = data.iloc[data.index[0:1460]] 
test = data.iloc[data.index[1460:]]
print(train.info())
print(test.info())
target = 'SalePrice'



## 3. Simple Linear Regression ##

import matplotlib.pyplot as plt
# For prettier plots.
import seaborn
fig = plt.figure(figsize=(19,6))
ax1 = fig.add_subplot(1,3,1)
ax1.scatter(x=train["Garage Area"],y=train["SalePrice"])
ax2 = fig.add_subplot(1,3,2) 
ax2.scatter(x=train["Gr Liv Area"],y=train["SalePrice"])
ax3=fig.add_subplot(1,3,3)
ax3.scatter(x=train["Overall Cond"],y=train["SalePrice"])
plt.show()


## 5. Using Scikit-Learn To Train And Predict ##

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit( train[["Gr Liv Area"]],  train["SalePrice"])
a1 = lr.coef_
a0 = lr.intercept_
print(a1)
print(a0)



## 6. Making Predictions ##

import numpy as np
from sklearn.metrics import mean_squared_error

lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])
train_predict = lr.predict(train[["Gr Liv Area"]])
test_predict = lr.predict(test[["Gr Liv Area"]])
train_mse = mean_squared_error(train_predict,train["SalePrice"])
test_mse = mean_squared_error(test_predict,test["SalePrice"])

train_rmse = train_mse**(1/2)
test_rmse = test_mse**(1/2)

print(train_rmse)
print(test_rmse)

## 7. Multiple Linear Regression ##

cols = ['Overall Cond', 'Gr Liv Area']

lr = LinearRegression()
lr.fit(train[cols],train["SalePrice"])

train_predict = lr.predict(train[cols])
test_predict = lr.predict(test[cols])

train_mse = mean_squared_error(train_predict,train["SalePrice"])
test_mse = mean_squared_error(test_predict,test["SalePrice"])

train_rmse_2 = train_mse**(1/2)
test_rmse_2 = test_mse**(1/2)

print(train_rmse_2)
print(test_rmse_2)