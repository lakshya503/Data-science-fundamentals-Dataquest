## 3. Bias-variance tradeoff ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

def train_and_test(cols):
    lr = LinearRegression()
    lr.fit(filtered_cars[cols], filtered_cars["mpg"])
    predictions = lr.predict(filtered_cars[cols])
    mse = mean_squared_error(predictions,filtered_cars["mpg"])
    variance = np.var(predictions)
    return(mse,variance)
cyl_mse,cyl_var = train_and_test(["cylinders"])
print(cyl_mse,cyl_var)
weight_mse,weight_var = train_and_test(["weight"])

## 4. Multivariate models ##

# Our implementation for train_and_test, takes in a list of strings.
def train_and_test(cols):
    # Split into features & target.
    features = filtered_cars[cols]
    target = filtered_cars["mpg"]
    # Fit model.
    lr = LinearRegression()
    lr.fit(features, target)
    # Make predictions on training set.
    predictions = lr.predict(features)
    # Compute MSE and Variance.
    mse = mean_squared_error(filtered_cars["mpg"], predictions)
    variance = np.var(predictions)
    return(mse, variance)

one_mse, one_var = train_and_test(["cylinders"])
print(one_mse,one_var)
two_mse,two_var = train_and_test(["cylinders","displacement"])
print(two_mse,two_var)
three_mse, three_var = train_and_test(["cylinders","displacement","horsepower"])
print(three_mse,three_var)
four_mse, four_var = train_and_test(["cylinders","displacement","horsepower","weight"])
print(four_mse,four_var)
five_mse,five_var = train_and_test(["cylinders","displacement","horsepower","weight","acceleration"])
print(five_mse,five_var)
six_mse, six_var = train_and_test(["cylinders","displacement","horsepower","weight","acceleration","model year"])
print(six_mse,six_var)
seven_mse, seven_var = train_and_test(["cylinders","horsepower", "displacement","weight", "acceleration", "model year", "origin"])
print(seven_mse,seven_var)

## 5. Cross validation ##

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score

import numpy as np

def train_and_cross_val(cols):
    kf = KFold(n_splits = 10, shuffle = True, random_state = 3) 
    lr = LinearRegression()
    features = filtered_cars[cols]
    target = filtered_cars["mpg"]
    mse = []
    var = []
    
    for i,j in kf.split(features):
        x_train = features.iloc[i]
        x_test = features.iloc[j]
        y_train = target.iloc[i]
        y_test = target.iloc[j] 
        
        lr.fit(x_train,y_train)
        predictions = lr.predict(x_test) 
        
        mse.append(mean_squared_error(predictions, y_test))
        var.append(np.var(predictions))
        
    ave_mse = np.mean(mse)
    ave_var=np.mean(var) 
    
    return(ave_mse,ave_var)

two_mse,two_var = train_and_cross_val(["cylinders","displacement"])
print(two_mse,two_var)
three_mse,three_var = train_and_cross_val(["cylinders","displacement","horsepower"])
print(three_mse,three_var)
four_mse,four_var = train_and_cross_val(["cylinders","displacement","horsepower","weight"])
print(four_mse,four_var)
five_mse,five_var = train_and_cross_val(["cylinders","displacement","horsepower","weight","acceleration"])
print(five_mse,five_var)
six_mse,six_var = train_and_cross_val(["cylinders","displacement","horsepower","weight","acceleration","model year"])
print(six_mse,six_var)
seven_mse,seven_var =train_and_cross_val(["cylinders","horsepower","displacement","weight","acceleration","model year","origin"])
print(seven_mse,seven_var)



## 6. Plotting cross-validation error vs. cross-validation variance ##

# We've hidden the `train_and_cross_val` function to save space but you can still call the function!
import matplotlib.pyplot as plt
        
two_mse, two_var = train_and_cross_val(["cylinders", "displacement"])
three_mse, three_var = train_and_cross_val(["cylinders", "displacement", "horsepower"])
four_mse, four_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight"])
five_mse, five_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration"])
six_mse, six_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year"])
seven_mse, seven_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration","model year", "origin"])

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

mses = [two_mse,three_mse,four_mse,five_mse,six_mse,seven_mse]
var = [two_var,three_var, four_var,five_var,six_var,seven_var]
num = np.arange(2,8,1)

ax1.scatter(x = num , y = mses , c="red")
ax1.scatter(x = num  , y = var  , c = "blue")
plt.show()