## 1. Recap ##

import pandas as pd
import numpy as np
np.random.seed(1)

dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

dc_listings.info()

## 2. Removing features ##

dc_listings = dc_listings.drop(["room_type","city","state","latitude","longitude","zipcode","host_response_rate","host_acceptance_rate","host_listings_count"],axis = 1)


## 3. Handling missing values ##

dc_listings = dc_listings.drop(["cleaning_fee" , "security_deposit"],axis=1)
dc_listings = dc_listings.dropna(axis = 0)


## 4. Normalize columns ##

normalized_listings = pd.DataFrame()
normalized_listings = (dc_listings-dc_listings.mean())/dc_listings.std()
normalized_listings["price"] = dc_listings["price"]
print(dc_listings.head(3))

## 5. Euclidean distance for multivariate case ##

from scipy.spatial import distance

first_list = (normalized_listings.iloc[0][["accommodates","bathrooms"]])
fifth_list = (normalized_listings.iloc[4][["accommodates","bathrooms"]])

first_fifth_distance = distance.euclidean(first_list,fifth_list)


## 7. Fitting a model and making predictions ##

from sklearn.neighbors import KNeighborsRegressor

train_df = normalized_listings.iloc[0:2792]
test_df = normalized_listings.iloc[2792:]

knn = KNeighborsRegressor(n_neighbors=5,algorithm="brute")
train_val = train_df[["accommodates","bathrooms"]]
train_tar = train_df["price"]

knn.fit(train_val,train_tar)
predictions = knn.predict(test_df[["accommodates","bathrooms"]])

## 8. Calculating MSE using Scikit-Learn ##

from sklearn.metrics import mean_squared_error

train_columns = ['accommodates', 'bathrooms']
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute', metric='euclidean')
knn.fit(train_df[train_columns], train_df['price'])
predictions = knn.predict(test_df[train_columns])

two_features_mse = mean_squared_error(test_df["price"],predictions)
two_features_rmse = np.sqrt(two_features_mse)

print(two_features_mse)
print(two_features_rmse)

## 9. Using more features ##

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')

train_val = train_df[["accommodates","bedrooms","bathrooms","number_of_reviews"]]
train_targ = train_df["price"]
knn.fit(train_val,train_targ)
four_predictions = knn.predict(test_df[["accommodates","bedrooms","bathrooms","number_of_reviews"]])

four_mse = mean_squared_error(test_df["price"], four_predictions)
four_rmse = four_mse**(1/2)

print(four_mse)
print(four_rmse)

## 10. Using all features ##

print(train_df)
knn=KNeighborsRegressor(n_neighbors=5,algorithm="brute")
features = train_df.columns.tolist()
features.remove('price')

train_targ = train_df["price"] 

knn.fit(train_df[features],train_targ)
all_features_predictions = knn.predict(test_df[features])

all_features_mse = mean_squared_error(test_df["price"],all_features_predictions)
all_features_rmse = all_features_mse**(1/2)