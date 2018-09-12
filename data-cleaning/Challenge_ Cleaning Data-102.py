## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()

print(avengers.columns)

true_avengers = avengers.loc[avengers["Year"]>=1960,:]
print(true_avengers.head())


## 5. Consolidating Deaths ##

print(avengers.columns)
def fun(row):
    count = 0
    cols =["Death1" , "Death2","Death3", "Death4", "Death5"] 
    for i in cols:
        if row[i]=="YES":
            count = count +1
        else:
            continue
    return count

true_avengers["Deaths"] = true_avengers.apply(fun,axis=1)

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()
count = 0
def fun(row):
    if 2015-int(row["Year"]) == int(row["Years since joining"]):
        return count+1
    else:
        return count
joined_accuracy_count = true_avengers.apply(fun, axis = 1).count()
        