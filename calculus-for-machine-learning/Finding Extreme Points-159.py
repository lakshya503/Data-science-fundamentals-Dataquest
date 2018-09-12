## 3. Differentiation ##

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,6,110)
y = -2*x + 3 
fig = plt.figure()
ax = plt.axes()
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.plot(x,y) 
plt.show()


## 6. Power Rule ##

import sympy 
slope_one = 80
slope_two = 0

## 7. Linearity Of Differentiation ##

slope_three = 4
slope_four = 8

## 8. Practicing Finding Extreme Values ##

rel_min = []
rel_max =[] 
rel_min.append(2/3)
rel_max.append(0)