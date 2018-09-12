## 1. Introduction to the data ##

import pandas as pd
cars = pd.read_csv("auto.csv")
unique_regions = cars["origin"].unique()
print(unique_regions)

## 2. Dummy variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)
dummy_years =pd.get_dummies(cars["year"] , prefix = "year")
cars = pd.concat([cars,dummy_years],axis=1) 
cars = cars.drop(["year","cylinders"] , axis=1)
print(cars.head(5))


## 3. Multiclass classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]

point= int(0.7*len(shuffled_cars))

train = shuffled_cars[0:point]
test = shuffled_cars[point:]

## 4. Training a multiclass logistic regression model ##

from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()

features = [x for x in cars.columns if x.startswith('cyl') or x.startswith('year')]
models = {}
for i in unique_origins:
    lr = LogisticRegression()
    lr.fit(train[features],train["origin"]==i)
    models[i] = lr
    

## 5. Testing the models ##

testing_probs = pd.DataFrame(columns=unique_origins)
print(testing_probs)
for i in unique_origins:
    predictions = models[i].predict_proba(test[features])
    print("-" *10)
    print(predictions[:,1])
    testing_probs[i] = predictions[:,1]
    

## 6. Choose the origin ##

print(testing_probs)
predicted_origins = testing_probs.idxmax(axis=1)
print(predicted_origins)
    