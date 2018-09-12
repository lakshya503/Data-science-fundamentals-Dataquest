## 2. Inconsistent Systems ##

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,20,1000)
y1 = (5-8*x)/4
y2 = (5-4*x)/2
fig = plt.figure()
ax = plt.axes() 
ax.plot(x,y1,color="blue")
ax.plot(x,y2,color="blue") 
plt.show()


## 5. Homogenous Systems ##

def test_homog(x3):
    x1 = 4*x3/3
    x2 = 0 
    return ((3*x1+5*x2-4*x3==0) and (3*x2==0))
b_one = test_homog(1)
b_two = test_homog(-10)