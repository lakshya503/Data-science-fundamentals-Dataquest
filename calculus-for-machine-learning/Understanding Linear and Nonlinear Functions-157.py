## 1. Why Learn Calculus? ##

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,3,num=301)
y = -(x**2)+3*x-1
plt.plot(x,y)
plt.show()

## 4. Math Behind Slope ##

def slope(x1,x2,y1,y2):
    ## Finish the function here
    return 0
slope_one = slope(0,4,1,13)
slope_two = slope(5,-1,16,-2)

def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

slope_one = slope(0,1,4,13)
slope_two = slope(5,16,-1,-2)

## 6. Secant Lines ##

import seaborn
seaborn.set(style='darkgrid')

def draw_secant(x_values):
    x = np.linspace(-20,30,100)
    y = -1*(x**2) + x*3 - 1
    plt.plot(x,y)
    x_0 = x_values[0]
    x_1 = x_values[1] 
    y_0 = -1*(x_0**2)+x_0*3 - 1
    y_1 = -1*(x_1**2)+x_1*3 - 1
    m = (y_1 - y_0)/(x_1-x_0)
    b = y_0 - m*x_0 
    y_sec = x*m+b
    plt.plot(x,y_sec,c="green")
    
    # Add your code here.
    
    plt.show()
line1 = draw_secant([3,5])
line2=draw_secant([3,10])
line3=draw_secant([3,15])