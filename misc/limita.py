#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 22:18:33 2019

@author: mh70
"""


# x = 0.423361075101
def f(x):
    suma = 0
    for i in range(30):
        suma += (x**(i+1) + 3*x**(i+2))
    return suma

target = 5/3

init = 0
delta = 0.1
y = init
y_high = y_low = 0

for i in range(100):
    result = f(y)
    print(result, y)

    if result > target:
        y -= delta
        if y_high == y:
            delta /= 4
            y += delta
        y_high = y
    else:
        y += delta
        if y_low == y:
            delta /= 4
            y -= delta
        y_low = y
