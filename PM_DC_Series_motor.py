# -*- coding: utf-8 -*-
"""
Created on Mon May 22 18:11:25 2023

@author: Lenovo
"""

# Plottinng the Permanent magnet DC Series motor 

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# dw/dt =  d^2(0)/ dt^2
def fnctn(w,t,ir,u,Tm,Te):
    dxdt = [w[1] , (Tm/Te)*(-w[0] - ir - u)]
    return dxdt

# Taking Parameters from the paper 
r = 5.35
L=3.93e-3
J=2.75e-6 
k=0.0316  
Tm = (J*r)/(k*r**2)
Te = L/r
u = 12
ir = 2
t = np.linspace(0,200,100)
y0 = [0,1]


soln = odeint(fnctn, y0 , t, args = (u,ir,Tm,Te))


# Plotting the soloution vs y_1 and y_2 respectively
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

plt.plot(t,soln[:,0],'r', label = 'x1')
plt.plot(t,soln[:,1],'b', label = 'x2')
plt.grid()
plt.show()

# Plotting soloution y_1 vs y_2
plt.plot(soln[:,0],soln[:,1],'-k' , 'c', markersize = '2')
plt.grid()
plt.xlabel('y(1)')
plt.ylabel('y(2)')