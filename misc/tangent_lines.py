#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 23:06:16 2018
http://math-physics-problems.wikia.com/wiki/Graphing_Tangent_Lines_with_Python
@author: mh70
"""

import matplotlib.pyplot as plt
import numpy as np

def deriv(f, x):
    
    h = 0.000_000_001  #step-size
    return (f(x+h) - f(x))/h #definition of derivative

def deriv_left(f, x):
    
    h = 0.000_000_001  #step-size
    return (f(x) - f(x-h))/h #definition of derivative

def tangent_line(f, x_0, a, b):
    x = np.linspace(a, b, 200)
    y = f(x)
    y_0 = f(x_0)
    y_tan = deriv(f, x_0) * (x - x_0) + y_0
    
    #plotting
    plt.plot(x, y, "r-")
    plt.plot(x, y_tan, "b-")
    plt.axis([a, b, a, b])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Plot of function with tangent line")
    plt.show()
    
def f1(x):
    return x**2

def f2(x):
    return np.exp(-x**2)

tangent_line(f1, 1, -2, 2)
tangent_line(f2, -1.5, -2, 2)

d1 = deriv(f1, 1)
d1_left = deriv_left(f1, 1)




max([deriv(f1, x) -  deriv_left(f1, x) for x in np.linspace(-2, 2, 200)])

max([deriv(f2, x) -  deriv_left(f2, x) for x in np.linspace(-2, 2, 200)])