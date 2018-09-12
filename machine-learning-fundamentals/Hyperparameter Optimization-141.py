## 1. Recap ##

import pandas as pd
train_df = pd.read_csv("dc_airbnb_train.csv")
test_df = pd.read_csv("dc_airbnb_test.csv")

## 2. Hyperparameter optimization ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

hyper_params = [1,2,3,4,5]
mse_values =[]
for i in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=i,algorithm="brute")
    train_val = train_df[["accommodates","bedrooms","bathrooms","number_of_reviews"]]
    train_tar = train_df["price"] 
    knn.fit(train_val,train_tar)
    predictions = knn.predict(test_df[["accommodates","bedrooms","bathrooms","number_of_reviews"]])
    val = (mean_squared_error(test_df["price"],predictions))
    mse_values.append(val)   
print(mse_values)
        

## 3. Expanding grid search ##

import numpy as np
hyper_params = np.arange(1,21)
mse_values =[]
for i in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=i,algorithm="brute")
    train_val = train_df[["accommodates","bedrooms","bathrooms","number_of_reviews"]]
    train_tar = train_df["price"] 
    knn.fit(train_val,train_tar)
    predictions = knn.predict(test_df[["accommodates","bedrooms","bathrooms","number_of_reviews"]])
    val = (mean_squared_error(test_df["price"],predictions))
    mse_values.append(val)   
print(mse_values)

## 4. Visualizing hyperparameter values ##

import matplotlib.pyplot as plt
%matplotlib inline

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
hyper_params = [x for x in range(1, 21)]
mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df['price'], predictions)
    mse_values.append(mse)
    
plt.scatter(x=hyper_params, y=mse_values)
plt.show()

## 5. Varying features and hyperparameters ##

hyper_params = [x for x in range(1,21)]
features = train_df.columns.tolist()
features.remove('price')
mse_values = list()
for i in hyper_params:
    knn = KNeighborsRegressor(n_neighbors = i, algorithm ="brute")
    train_tar = train_df["price"] 
    knn.fit(train_df[features],train_tar)
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(predictions,test_df["price"])
    mse_values.append(mse)
plt.scatter(x=hyper_params,y=mse_values)
plt.show()

## 6. Practice the workflow ##

two_features = ['accommodates', 'bathrooms']
three_features = ['accommodates', 'bathrooms', 'bedrooms']
hyper_params = [x for x in range(1,21)]
# Append the first model's MSE values to this list.
two_mse_values = list()
# Append the second model's MSE values to this list.
three_mse_values = list()
two_hyp_mse = dict()
three_hyp_mse = dict()


for i in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=i,algorithm="brute")
    train_val = train_df[two_features]
    train_tar = train_df["price"]
    knn.fit(train_val,train_tar)
    predictions = knn.predict(test_df[two_features])
    mse = mean_squared_error(predictions,test_df["price"])
    two_mse_values.append(mse)
min_ele = two_mse_values[0]
lowest_k = 1
for k,mse in enumerate(two_mse_values):
    if mse<min_ele:
        min_ele = mse 
        lowest_k = k+1
two_hyp_mse[lowest_k]=min_ele 



for j in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=j,algorithm="brute")

    knn.fit(train_df[three_features],train_df["price"])
    predictions = knn.predict(test_df[three_features])
    mse = mean_squared_error(test_df["price"],predictions)
    three_mse_values.append(mse)
    
min_ele= three_mse_values[0]

lowest_k = 1
for k,mse in enumerate(three_mse_values):
    
    if mse<min_ele:
        min_ele = mse 
        lowest_k = k+1
three_hyp_mse[lowest_k]=min_ele 
