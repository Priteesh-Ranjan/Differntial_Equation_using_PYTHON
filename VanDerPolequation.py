# -*- coding: utf-8 -*-
"""
Created on Mon May 22 17:07:52 2023

@author: Lenovo
"""

# Vanderpol Equation 

## Solving Differential Equation

# Importing Required Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# definiing the VanDerPol Equation

def fnctn(y,t,k1,k2):
    dxdt = [y[1] , k1*(1-(y[0]**2))*y[1] - k2*y[0]]
    return dxdt

# Setting the initial values 
y0 = [0,1]
t = np.linspace(0,10,1000)
k1 = 1
k2 = 1

# using odeint function to solve the ordinary diffferntial Equation
soloutionode = odeint(fnctn, y0 , t, args = (k1,k2))

# Plotting the soloution vs y_1 and y_2 respectively

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.plot(t,soloutionode[:,0],'r', label = 'x1')
plt.plot(t,soloutionode[:,1],'b', label = 'x2')
plt.grid()
plt.show()

# Plotting soloution y_1 vs y_2
plt.plot(soloutionode[:,0],soloutionode[:,1],'.' , 'c', markersize = '2')
plt.savefig('w vs t', dpi =1500)
plt.grid()
plt.xlabel('y(1)')
plt.ylabel('y(2)')
