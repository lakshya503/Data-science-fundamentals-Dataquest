## 1. Introduction ##

import numpy as np
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')


      
shuffle = np.random.permutation(dc_listings.index)
dc_listings = dc_listings.reindex(shuffle)
new_dc = dc_listings.copy()

split_one = new_dc[0:1862]
split_two = new_dc[1862:]

## 2. Holdout Validation ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one

print(train_one.columns)

knn = KNeighborsRegressor()

knn.fit(train_one[["accommodates"]] ,train_one["price"])
test_one["predictions"] = knn.predict(test_one[["accommodates"]])
mse = mean_squared_error(test_one["price"],test_one["predictions"])
rmse = mse**(1/2)
iteration_one_rmse = rmse 





knn.fit(train_two[["accommodates"]],train_two["price"])
test_two["new_predictions"] = knn.predict(test_two[["accommodates"]])
new_mse = mean_squared_error(test_two["price"],test_two["new_predictions"])
iteration_two_rmse = new_mse**(1/2)

avg_rmse = np.mean([iteration_one_rmse,iteration_two_rmse])

## 3. K-Fold Cross Validation ##

dc_listings.loc[dc_listings.index[0:745], "fold"] = 1
dc_listings.loc[dc_listings.index[745:1490], "fold"] = 2
dc_listings.loc[dc_listings.index[1490:2234], "fold"] = 3
dc_listings.loc[dc_listings.index[2234:2978], "fold"] = 4
dc_listings.loc[dc_listings.index[2978:3723], "fold"] = 5



## 4. First iteration ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

knn = KNeighborsRegressor()
train_val = dc_listings[dc_listings["fold"]>1]
train_tar = dc_listings[dc_listings["fold"]>1]
knn.fit(train_val[["accommodates"]],train_tar[["price"]])
new_val = dc_listings[dc_listings["fold"]==1]
labels = knn.predict(new_val[["accommodates"]])

iteration_one_mse = mean_squared_error(new_val[["price"]],labels)
iteration_one_rmse = iteration_one_mse**(1/2)




## 5. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
fold_ids = [1,2,3,4,5]
rmses = [] 
fold_rmses =[]
def train_and_validate(df, fold_ids):
    knn = KNeighborsRegressor()
    for i in fold_ids:
        train_val = df[df["fold"]!=i]
        knn.fit(train_val[["accommodates"]],train_val["price"])
        test_val = df[df["fold"]==i]
        predictions= knn.predict(test_val[["accommodates"]])
        mse = mean_squared_error(test_val["price"],predictions)
        rmse = mse**(1/2)
        fold_rmses.append(rmse)
    return(fold_rmses)
        
rmses = train_and_validate(dc_listings,fold_ids)

print(rmses)

avg_rmse = np.mean(rmses)
print(avg_rmse)


## 6. Performing K-Fold Cross Validation Using Scikit-Learn ##

from sklearn.model_selection import cross_val_score, KFold

kf = KFold(5,shuffle=True,random_state = 1)
knn = KNeighborsRegressor()
mses = cross_val_score(knn,dc_listings[["accommodates"]],dc_listings["price"],scoring = "neg_mean_squared_error", cv = kf)
print(mses)

avg_rmse= [abs(x)**(1/2) for x in mses]
avg_rmse = np.mean(avg_rmse)

## 7. Exploring Different K Values ##

from sklearn.model_selection import cross_val_score, KFold

num_folds = [3, 5, 7, 9, 10, 11, 13, 15, 17, 19, 21, 23]

for fold in num_folds:
    kf = KFold(fold, shuffle=True, random_state=1)
    model = KNeighborsRegressor()
    mses = cross_val_score(model, dc_listings[["accommodates"]], dc_listings["price"], scoring="neg_mean_squared_error", cv=kf)
    rmses = np.sqrt(np.absolute(mses))
    avg_rmse = np.mean(rmses)
    std_rmse = np.std(rmses)
    print(str(fold), "folds: ", "avg RMSE: ", str(avg_rmse), "std RMSE: ", str(std_rmse))