## 1. Missing Values ##

import pandas as pd
data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

numerical_train=train.select_dtypes(include=["int","float"])
numerical_train.drop(["PID" , "Year Built", "Year Remod/Add", "Garage Yr Blt", "Mo Sold","Yr Sold"],inplace=True, axis = 1)
col_name = numerical_train.isnull().sum()
null_series = pd.Series(col_name)
print(null_series)
full_cols_series = null_series[null_series==0]
print(full_cols_series)



## 2. Correlating Feature Columns With Target Column ##

train_subset = train[full_cols_series.index]
new_corr = train_subset.corr()

sorted_corrs = abs(new_corr.loc["SalePrice"])
sorted_corrs = sorted_corrs.sort_values()
print(sorted_corrs)

## 3. Correlation Matrix Heatmap ##

import seaborn as sns
import matplotlib.pyplot as plt

strong_corrs= sorted_corrs[sorted_corrs>0.3]

new_train = train_subset[strong_corrs.index]
new_train=new_train.corr()
sns.heatmap(new_train)

## 4. Train And Test Model ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

final_corr_cols = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd'])
features = final_corr_cols.drop(['SalePrice']).index
target = 'SalePrice'


test = test[final_corr_cols.index]
test = test.dropna(axis=0)
clean_test = test

print(features)

lr = LinearRegression()
lr.fit(train[features] , train["SalePrice"])

train_predictions = lr.predict(train[features])
test_predictions = lr.predict(clean_test[features])

train_mse = mean_squared_error(train_predictions,train["SalePrice"])
test_mse = mean_squared_error(test_predictions,test["SalePrice"])

train_rmse = train_mse**(1/2)
test_rmse = test_mse**(1/2)



## 5. Removing Low Variance Features ##

train[features] = (train[features]-train[features].min())/(train[features].max()-train[features].min())


train_var = train[features].var()
sorted_vars= train_var.sort_values()

print(sorted_vars)

## 6. Final Model ##


print(sorted_vars.index)
features = features.drop(["Open Porch SF"])

lr=LinearRegression()
lr.fit(train[features],train["SalePrice"])

train_predictions = lr.predict(train[features])
test_predictions = lr.predict(clean_test[features])

train_mse = mean_squared_error(train_predictions,train["SalePrice"])
test_mse = mean_squared_error(test_predictions,clean_test["SalePrice"])

train_rmse_2 = train_mse**(1/2)
test_rmse_2 = test_mse**(1/2)

print(train_rmse_2)
print(test_rmse_2)