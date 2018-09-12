## 2. Introduction to the data ##

import pandas as pd
dc_listings = pd.read_csv("dc_airbnb.csv")
print(dc_listings.head())

## 4. Euclidean distance ##

import numpy as np
first_distance = (np.abs(dc_listings["accommodates"][0]-3))
print(first_distance)

## 5. Calculate distance for all observations ##

dc_listings["distance"] = abs(dc_listings["accommodates"]-3)
print(dc_listings["distance"].value_counts())

## 6. Randomizing, and sorting ##

import numpy as np
np.random.seed(1)
index = np.random.permutation(len(dc_listings))
dc_listings = dc_listings.loc[index]
dc_listings = dc_listings.sort_values(by = ["distance"])
print(dc_listings.head(10))

## 7. Average price ##

dc_listings["price"] = dc_listings["price"].str.replace("," , "")
dc_listings["price"] = dc_listings["price"].str.replace("$", "")
dc_listings["price"] = dc_listings["price"].astype(float)
print(dc_listings["price"])
mean_price = dc_listings["price"].head().mean()

## 8. Function to make predictions ##

# Brought along the changes we made to the `dc_listings` Dataframe.
dc_listings = pd.read_csv('dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

def predict_price(new_listing):
    temp_df = dc_listings.copy()
    ## Complete the function.
    temp_df["distance"] = abs(temp_df["accommodates"] - new_listing)

    temp_df = temp_df.sort_values(by = ["distance"])
    print(temp_df["price"])
    select_mean = temp_df["price"].head(5)
    print(select_mean)
    
    select_mean = select_mean.mean()
    return select_mean


acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)