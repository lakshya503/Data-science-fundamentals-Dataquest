## 1. Introduction ##

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

features = ['Wood Deck SF', 'Fireplaces', 'Full Bath', '1st Flr SF', 'Garage Area',
       'Gr Liv Area', 'Overall Qual']

X = train[features]
y = train["SalePrice"] 
optimal_val = np.dot(np.transpose(x),x)
inverse_optimal = np.linalg.inv(optimal_val)
second_half = np.dot(np.transpose(x), y) 

a = np.dot(inverse_optimal,second_half)