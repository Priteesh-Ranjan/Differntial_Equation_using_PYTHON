# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:15:39 2023

@author: Lenovo
"""

## Solving Differential Equation

# Importing Required Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

## Defining the Function 
def fnctn(x,t,k1,k2):
    dxdt = [x[1] , -k1*x[1]-k2*(np.sin(x[0]))]
    return dxdt

#setting the initial points 
x0 = [0,1]
t = np.linspace(0,100,20000)
k1 = 0.25
k2 = 0.5

# using odeint function to solve the ordinary diffferntial Equation

soloutionode = odeint(fnctn, x0, t, args = (k1,k2))

# Plotting the soloution vs y_1 and y_2 respectively
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.plot(t,soloutionode[:,0],'r', label = 'x1')
plt.plot(t,soloutionode[:,1],'b', label = 'x2')
plt.grid()
plt.savefig('Pendulum', dpi =500)
plt.show()

# Plotting the soloution vs y_1 and y_2 respectively
plt.plot(soloutionode[:,0],soloutionode[:,1],'-k' , 'c', markersize = '2')
plt.grid()
plt.xlabel('y(1)')
plt.ylabel('y(2)')
