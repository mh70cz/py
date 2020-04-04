#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 22:04:45 2018
prime using for else
@author: mh70
"""

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print (f"{n} is not a prime, it is divisible by {x}")
            break
    else:
        print (f"{n} is a prime")